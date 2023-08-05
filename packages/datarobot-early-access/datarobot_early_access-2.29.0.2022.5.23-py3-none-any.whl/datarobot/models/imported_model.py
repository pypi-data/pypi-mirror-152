#
# Copyright 2021 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# DataRobot, Inc.
#
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
#
# Released under the terms of DataRobot Tool and Utility Agreement.
import os

import trafaret as t

from datarobot._compat import String
from datarobot.utils.waiters import wait_for_async_resolution

from ..enums import DEFAULT_MAX_WAIT, DEFAULT_TIMEOUT
from ..utils import parse_time
from .api_object import APIObject


class ImportedModel(APIObject):
    """
    Represents an imported model available for making predictions. These are only relevant for
    administrators of on-premise Stand Alone Scoring Engines.

    ImportedModels are trained in one DataRobot application, exported as a `.drmodel` file, and
    then imported for use in a Stand Alone Scoring Engine.

    Attributes
    ----------
    id : str
        id of the import
    model_name : str
        model type describing the model generated by DataRobot
    display_name : str
        manually specified human-readable name of the imported model
    note : str
        manually added node about this imported model
    imported_at : datetime
        the time the model was imported
    imported_by_username : str
        username of the user who imported the model
    imported_by_id : str
        id of the user who imported the model
    origin_url : str
        URL of the application the model was exported from
    model_id : str
        original id of the model prior to export
    featurelist_name : str
        name of the featurelist used to train the model
    project_id : str
         id of the project the model belonged to prior to export
    project_name : str
        name of the project the model belonged to prior to export
    target : str
        the target of the project the model belonged to prior to export
    dataset_name : str
        filename of the dataset used to create the project the model belonged to
    created_by_username : str
        username of the user who created the model prior to export
    created_by_id : str
        id of the user who created the model prior to export
    """

    _root_path = "importedModels/"
    _converter = t.Dict(
        {
            t.Key("id"): String,
            t.Key("imported_at"): parse_time,
            t.Key("model_id"): String,
            t.Key("target"): String,
            t.Key("featurelist_name"): String,
            t.Key("dataset_name"): String,
            t.Key("model_name"): String,
            t.Key("project_id"): String,
            t.Key("note", optional=True, default=None): String | t.Null,  # from_api strips None
            t.Key("origin_url"): String,
            t.Key("imported_by_username"): String,
            t.Key("project_name"): String,
            t.Key("created_by_username"): String,
            t.Key("created_by_id"): String,
            t.Key("imported_by_id"): String,
            t.Key("display_name"): String,
        }
    ).allow_extra("*")

    def __init__(
        self,
        id,
        imported_at=None,
        model_id=None,
        target=None,
        featurelist_name=None,
        dataset_name=None,
        model_name=None,
        project_id=None,
        note=None,
        origin_url=None,
        imported_by_username=None,
        project_name=None,
        created_by_username=None,
        created_by_id=None,
        imported_by_id=None,
        display_name=None,
    ):

        self.id = id
        self.imported_at = imported_at
        self.model_id = model_id
        self.target = target
        self.featurelist_name = featurelist_name
        self.dataset_name = dataset_name
        self.model_name = model_name
        self.project_id = project_id
        self.note = note
        self.origin_url = origin_url
        self.imported_by_username = imported_by_username
        self.project_name = project_name
        self.created_by_username = created_by_username
        self.created_by_id = created_by_id
        self.imported_by_id = imported_by_id
        self.display_name = display_name

        self._path = self._get_path(id)

    @classmethod
    def create(cls, path, max_wait=DEFAULT_MAX_WAIT):
        """Import a previously exported model for predictions.

        Parameters
        ----------
        path : str
            The path to the exported model file
        max_wait : int, optional
            Time in seconds after which model import is considered unsuccessful
        """
        name = os.path.split(path)[1]
        response = cls._client.build_request_with_file(
            "post", cls._root_path, name, file_path=path, read_timeout=DEFAULT_TIMEOUT.UPLOAD
        )
        async_loc = response.headers["Location"]
        imported_model_loc = wait_for_async_resolution(cls._client, async_loc, max_wait=max_wait)
        return cls.from_location(imported_model_loc)

    @classmethod
    def _get_path(cls, id):
        return "{}{}/".format(cls._root_path, id)

    @classmethod
    def get(cls, import_id):
        """Retrieve imported model info

        Parameters
        ----------
        import_id : str
            The ID of the imported model.

        Returns
        -------
        imported_model : ImportedModel
            The ImportedModel instance
        """
        path = "{}{}/".format(cls._root_path, import_id)
        return cls.from_location(path)

    @classmethod
    def list(cls, limit=None, offset=None):
        """
        List the imported models.

        Parameters
        ----------
        limit : int
            The number of records to return. The server will use a (possibly finite) default if not
            specified.
        offset : int
            The number of records to skip.


        Returns
        -------
        imported_models : list[ImportedModel]
        """
        r_data = cls._client.get(cls._root_path, params={"limit": limit, "offset": offset}).json()
        return [cls.from_server_data(item) for item in r_data["data"]]

    def update(self, display_name=None, note=None):
        """
        Update the display name or note for an imported model. The ImportedModel object is updated
        in place.

        Parameters
        ----------
        display_name : str
            The new display name.
        note : str
            The new note.
        """
        self._client.patch(self._path, data={"display_name": display_name, "note": note})
        if display_name:  # Following pattern from Project.update. (Arguably technical debt.)
            self.display_name = display_name
        if note:
            self.note = note

    def delete(self):
        """
        Delete this imported model.
        """
        self._client.delete(self._path)

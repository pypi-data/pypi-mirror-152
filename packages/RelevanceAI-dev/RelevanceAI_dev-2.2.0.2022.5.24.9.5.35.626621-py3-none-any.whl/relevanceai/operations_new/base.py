"""
Base Operations Class
"""
from abc import ABC, abstractmethod

from typing import Any, Dict, List

from relevanceai.utils import DocUtils


class OperationBase(ABC, DocUtils):

    # Typehints to help with development
    vector_fields: List[str]
    alias: str

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.run(*args, **kwargs)

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def transform(self, *args, **kwargs) -> List[Dict[str, Any]]:
        """The function is an abstract method that raises a NotImplementedError if it is not implemented"""
        raise NotImplementedError

    def _check_vector_field_type(self):
        # check the vector fields
        if self.vector_fields is None:
            raise ValueError(
                "No vector_fields has been set. Please supply with vector_fields="
            )
        elif isinstance(self.vector_fields, str):
            # Force it to be a list instead
            self.vector_fields = [self.vector_fields]

    def _check_vector_names(self):
        if hasattr(self, "vector_fields"):
            for vector_field in self.vector_fields:
                if not vector_field.endswith("_vector_"):
                    raise ValueError(
                        "Invalid vector field. Ensure they end in `_vector_`."
                    )

    def _check_vector_field_in_schema(self):
        # TODO: check the schema
        if hasattr(self, "dataset"):
            for vector_field in self.vector_fields:
                if hasattr(self.dataset, "schema"):
                    assert vector_field in self.dataset.schema

    def _check_vector_fields(self):
        self._check_vector_field_type()

        if len(self.vector_fields) == 0:
            raise ValueError("No vector fields set. Please supply with vector_fields=")
        self._check_vector_names()
        self._check_vector_field_in_schema()

    def _check_alias(self):
        if self.alias is None:
            raise ValueError("alias is not set. Please supply alias=")
        if self.alias.lower() != self.alias:
            raise ValueError("Alias cannot be lower case.")

    def _get_package_from_model(self, model):
        """
        Determine the package for a model.
        This can be useful for checking dependencies.
        This may be used across modules for
        deeper integrations
        """
        # TODO: add support for huggingface integrations
        # such as transformers and sentencetransformers
        model_name = str(model.__class__).lower()
        if "function" in model_name:
            model_name = str(model.__name__)

        if "sklearn" in model_name:
            self.package = "sklearn"

        elif "faiss" in model_name:
            self.package = "faiss"

        elif "hdbscan" in model_name:
            self.package = "hdbscan"

        elif "communitydetection" in model_name:
            self.package = "sentence-transformers"

        else:
            self.package = "custom"
        return self.package

    @staticmethod
    def normalize_string(string: str):
        return string.lower().replace("-", "").replace("_", "")

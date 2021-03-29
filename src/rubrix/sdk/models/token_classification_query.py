from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.prediction_status import PredictionStatus
from ..models.task_status import TaskStatus
from ..models.token_classification_query_metadata import (
    TokenClassificationQueryMetadata,
)
from ..models.token_classification_query_query_text import (
    TokenClassificationQueryQueryText,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenClassificationQuery")


@attr.s(auto_attribs=True)
class TokenClassificationQuery:
    """Filters for token classification API

    Attributes:
    -----------

    text_query: Union[str, Dict[str, str]]
        Text query over input tokens

    metadata: Optional[Dict[str, Union[str, List[str]]]]
        Text query over metadata fields. Default=None"""

    predicted_as: Union[Unset, List[str]] = UNSET
    annotated_as: Union[Unset, List[str]] = UNSET
    annotated_by: Union[Unset, List[str]] = UNSET
    predicted_by: Union[Unset, List[str]] = UNSET
    status: Union[Unset, List[TaskStatus]] = UNSET
    predicted: Union[Unset, PredictionStatus] = UNSET
    query_text: Union[Unset, str, TokenClassificationQueryQueryText] = UNSET
    metadata: Union[TokenClassificationQueryMetadata, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        predicted_as: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.predicted_as, Unset):
            predicted_as = self.predicted_as

        annotated_as: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.annotated_as, Unset):
            annotated_as = self.annotated_as

        annotated_by: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.annotated_by, Unset):
            annotated_by = self.annotated_by

        predicted_by: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.predicted_by, Unset):
            predicted_by = self.predicted_by

        status: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = []
            for status_item_data in self.status:
                status_item = status_item_data.value

                status.append(status_item)

        predicted: Union[Unset, PredictionStatus] = UNSET
        if not isinstance(self.predicted, Unset):
            predicted = self.predicted

        query_text: Union[Unset, str, TokenClassificationQueryQueryText]
        if isinstance(self.query_text, Unset):
            query_text = UNSET
        elif isinstance(self.query_text, TokenClassificationQueryQueryText):
            query_text = UNSET
            if not isinstance(self.query_text, Unset):
                query_text = self.query_text.to_dict()

        else:
            query_text = self.query_text

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if predicted_as is not UNSET:
            field_dict["predicted_as"] = predicted_as
        if annotated_as is not UNSET:
            field_dict["annotated_as"] = annotated_as
        if annotated_by is not UNSET:
            field_dict["annotated_by"] = annotated_by
        if predicted_by is not UNSET:
            field_dict["predicted_by"] = predicted_by
        if status is not UNSET:
            field_dict["status"] = status
        if predicted is not UNSET:
            field_dict["predicted"] = predicted
        if query_text is not UNSET:
            field_dict["query_text"] = query_text
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        predicted_as = cast(List[str], d.pop("predicted_as", UNSET))

        annotated_as = cast(List[str], d.pop("annotated_as", UNSET))

        annotated_by = cast(List[str], d.pop("annotated_by", UNSET))

        predicted_by = cast(List[str], d.pop("predicted_by", UNSET))

        status = []
        _status = d.pop("status", UNSET)
        for status_item_data in _status or []:
            status_item = TaskStatus(status_item_data)

            status.append(status_item)

        predicted: Union[Unset, PredictionStatus] = UNSET
        _predicted = d.pop("predicted", UNSET)
        if not isinstance(_predicted, Unset):
            predicted = PredictionStatus(_predicted)

        def _parse_query_text(
            data: Any,
        ) -> Union[Unset, str, TokenClassificationQueryQueryText]:
            data = None if isinstance(data, Unset) else data
            query_text: Union[Unset, str, TokenClassificationQueryQueryText]
            try:
                query_text = UNSET
                _query_text = data
                if not isinstance(_query_text, Unset):
                    query_text = TokenClassificationQueryQueryText.from_dict(
                        _query_text
                    )

                return query_text
            except:  # noqa: E722
                pass
            return cast(Union[Unset, str, TokenClassificationQueryQueryText], data)

        query_text = _parse_query_text(d.pop("query_text", UNSET))

        metadata: Union[TokenClassificationQueryMetadata, Unset] = UNSET
        _metadata = d.pop("metadata", UNSET)
        if not isinstance(_metadata, Unset):
            metadata = TokenClassificationQueryMetadata.from_dict(_metadata)

        token_classification_query = cls(
            predicted_as=predicted_as,
            annotated_as=annotated_as,
            annotated_by=annotated_by,
            predicted_by=predicted_by,
            status=status,
            predicted=predicted,
            query_text=query_text,
            metadata=metadata,
        )

        token_classification_query.additional_properties = d
        return token_classification_query

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from typing import Dict, Optional, Union

from pydantic import Field
from rubrix.server.commons.models import BaseModel, List, SortParam
from rubrix.server.dataset_records.model import (
    BaseTaskSearchAggregations,
    DefaultTaskSearchFilters,
)
from rubrix.server.datasets.model import UpdateDatasetRequest

from .model import TokenClassificationRecord


class TokenClassificationBulkData(UpdateDatasetRequest):
    """
    Bulk data for text classification

    Attributes:
    -----------

    records: List[TokenClassificationRecord]
        Set of token classification records

    """

    records: List[TokenClassificationRecord]


class TokenClassificationQuery(DefaultTaskSearchFilters):
    """
    Filters for token classification API

    Attributes:
    -----------

    text_query: Union[str, Dict[str, str]]
        Text query over input tokens

    metadata: Optional[Dict[str, Union[str, List[str]]]]
        Text query over metadata fields. Default=None

    """

    text_query: Union[str, Dict[str, str]] = Field(
        default_factory=dict, alias="query_text"
    )
    metadata: Optional[Dict[str, Union[str, List[str]]]] = None

    class Config:
        allow_population_by_field_name = True


class TokenClassificationAggregations(BaseTaskSearchAggregations):
    """
    Search results for token classification search API

    Attributes:
    -----------

    words: WordCloudAggregations
        The word cloud aggregations (grouped by language)

    metadata: Dict[str, Dict[str, int]]
        The metadata fields aggregations

    """

    words: Dict[str, int] = Field(default_factory=dict)
    metadata: Dict[str, Dict[str, int]] = Field(default_factory=dict)


class TokenClassificationSearchRequest(BaseModel):
    """
    API Search request

    Attributes:
    -----------

    query: TokenClassificationQuery
        The search query configuration

    sort: List[SortParam]
        The sort params to use for record results

    """

    query: TokenClassificationQuery = Field(default_factory=TokenClassificationQuery)
    sort: List[SortParam] = Field(default_factory=list)


class TokenClassificationSearchResults(BaseModel):
    """
    API search results

    Attributes:
    -----------

    total: int
        The total number of records
    records: List[TextClassificationRecord]
        The selected records to return
    aggregations: TextClassificationAggregations
        Search aggregations (if no pagination)

    """

    total: int = 0
    records: List[TokenClassificationRecord] = Field(default_factory=list)
    aggregations: TokenClassificationAggregations = None

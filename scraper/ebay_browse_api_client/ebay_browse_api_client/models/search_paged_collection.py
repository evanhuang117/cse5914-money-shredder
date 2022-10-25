from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.auto_corrections import AutoCorrections
from ..models.error import Error
from ..models.item_summary import ItemSummary
from ..models.refinement import Refinement
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchPagedCollection")


@attr.s(auto_attribs=True)
class SearchPagedCollection:
    """The type that defines the fields for a paginated result set. The response consists of 0 or more sequenced <em>
    pages</em> where each page has 0 or more items.

        Attributes:
            auto_corrections (Union[Unset, AutoCorrections]):
            href (Union[Unset, str]): The URI of the current page of results. <br /><br />The following example of the <b>
                search</b> method returns items 1 thru 5 from the list of items found. <br /><br
                /><code>https://api.ebay.com/buy/v1/item_summary/search?q=shirt&limit=5&offset=0</code>.
            item_summaries (Union[Unset, List[ItemSummary]]): An array of the items on this page. The items are sorted
                according to the sorting method specified in the request.
            limit (Union[Unset, int]): The value of the <b>limit</b> parameter submitted in the request, which is the
                maximum number of items to return on a page, from the result set. A result set is the complete set of items
                returned by the method.
            next_ (Union[Unset, str]): The URI for the next page of results. This value is returned if there is an
                additional page of results to return from the result set. <br /><br />The following example of the <b>
                search</b> method returns items 5 thru 10 from the list of items found.<br /> <br
                /><code>https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&limit=5&offset=10 </code>
            offset (Union[Unset, int]): This value indicates the <b>offset</b> used for current page of items being
                returned. Assume the initial request used an <b>offset</b> of <code>0</code> and a <b>limit</b> of
                <code>3</code>. Then in the first page of results, this value would be <code>0</code>, and items 1-3 are
                returned. For the second page, this value is <code>3</code> and so on.
            prev (Union[Unset, str]): The URI for the previous page of results. This is returned if there is a previous page
                of results from the result set. <br /><br />The following example of the <b> search</b> method returns items 1
                thru 5 from the list of items found, which would be the first set of items returned.<br /> <br
                /><code>https://api.ebay.com/buy/v1/item_summary/search?query=t-shirts&limit=5&offset=0</code>
            refinement (Union[Unset, Refinement]): This type defines the fields for the various refinements of an item. You
                can use the information in this container to create histograms, which help shoppers choose exactly what they
                want.
            total (Union[Unset, int]): The total number of items that match the input criteria.
            warnings (Union[Unset, List[Error]]): The container with all the warnings for the request.
    """

    auto_corrections: Union[Unset, AutoCorrections] = UNSET
    href: Union[Unset, str] = UNSET
    item_summaries: Union[Unset, List[ItemSummary]] = UNSET
    limit: Union[Unset, int] = UNSET
    next_: Union[Unset, str] = UNSET
    offset: Union[Unset, int] = UNSET
    prev: Union[Unset, str] = UNSET
    refinement: Union[Unset, Refinement] = UNSET
    total: Union[Unset, int] = UNSET
    warnings: Union[Unset, List[Error]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_corrections: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_corrections, Unset):
            auto_corrections = self.auto_corrections.to_dict()

        href = self.href
        item_summaries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.item_summaries, Unset):
            item_summaries = []
            for item_summaries_item_data in self.item_summaries:
                item_summaries_item = item_summaries_item_data.to_dict()

                item_summaries.append(item_summaries_item)

        limit = self.limit
        next_ = self.next_
        offset = self.offset
        prev = self.prev
        refinement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.refinement, Unset):
            refinement = self.refinement.to_dict()

        total = self.total
        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()

                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_corrections is not UNSET:
            field_dict["autoCorrections"] = auto_corrections
        if href is not UNSET:
            field_dict["href"] = href
        if item_summaries is not UNSET:
            field_dict["itemSummaries"] = item_summaries
        if limit is not UNSET:
            field_dict["limit"] = limit
        if next_ is not UNSET:
            field_dict["next"] = next_
        if offset is not UNSET:
            field_dict["offset"] = offset
        if prev is not UNSET:
            field_dict["prev"] = prev
        if refinement is not UNSET:
            field_dict["refinement"] = refinement
        if total is not UNSET:
            field_dict["total"] = total
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _auto_corrections = d.pop("autoCorrections", UNSET)
        auto_corrections: Union[Unset, AutoCorrections]
        if isinstance(_auto_corrections, Unset):
            auto_corrections = UNSET
        else:
            auto_corrections = AutoCorrections.from_dict(_auto_corrections)

        href = d.pop("href", UNSET)

        item_summaries = []
        _item_summaries = d.pop("itemSummaries", UNSET)
        for item_summaries_item_data in _item_summaries or []:
            item_summaries_item = ItemSummary.from_dict(item_summaries_item_data)

            item_summaries.append(item_summaries_item)

        limit = d.pop("limit", UNSET)

        next_ = d.pop("next", UNSET)

        offset = d.pop("offset", UNSET)

        prev = d.pop("prev", UNSET)

        _refinement = d.pop("refinement", UNSET)
        refinement: Union[Unset, Refinement]
        if isinstance(_refinement, Unset):
            refinement = UNSET
        else:
            refinement = Refinement.from_dict(_refinement)

        total = d.pop("total", UNSET)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        search_paged_collection = cls(
            auto_corrections=auto_corrections,
            href=href,
            item_summaries=item_summaries,
            limit=limit,
            next_=next_,
            offset=offset,
            prev=prev,
            refinement=refinement,
            total=total,
            warnings=warnings,
        )

        search_paged_collection.additional_properties = d
        return search_paged_collection

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

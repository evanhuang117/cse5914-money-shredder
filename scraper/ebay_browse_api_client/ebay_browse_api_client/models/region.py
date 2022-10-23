from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Region")


@attr.s(auto_attribs=True)
class Region:
    """This type is used to provide region details for a tax jurisdiction.

    Attributes:
        region_name (Union[Unset, str]): A localized text string that indicates the name of the region. Taxes are
            generally charged at the state/province level or at the country level in the case of VAT tax.
        region_type (Union[Unset, str]): An enumeration value that indicates the type of region for the tax
            jurisdiction. <br><br><b> Valid Values: </b> <ul><li><b> STATE_OR_PROVINCE </b> - Indicates the region is a
            state or province within a country, such as California or New York in the US, or Ontario or Alberta in
            Canada.</li><li><b> COUNTRY </b> - Indicates the region is a single country.</li></ul>  Code so that your app
            gracefully handles any future changes to this list. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/ba:RegionTypeEnum'>eBay API documentation</a>
    """

    region_name: Union[Unset, str] = UNSET
    region_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_name = self.region_name
        region_type = self.region_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_name is not UNSET:
            field_dict["regionName"] = region_name
        if region_type is not UNSET:
            field_dict["regionType"] = region_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_name = d.pop("regionName", UNSET)

        region_type = d.pop("regionType", UNSET)

        region = cls(
            region_name=region_name,
            region_type=region_type,
        )

        region.additional_properties = d
        return region

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

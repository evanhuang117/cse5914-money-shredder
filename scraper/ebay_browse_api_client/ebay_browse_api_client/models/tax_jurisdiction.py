from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.region import Region
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxJurisdiction")


@attr.s(auto_attribs=True)
class TaxJurisdiction:
    """The type that defines the fields for the tax jurisdiction details.

    Attributes:
        region (Union[Unset, Region]): This type is used to provide region details for a tax jurisdiction.
        tax_jurisdiction_id (Union[Unset, str]): The identifier of the tax jurisdiction.
    """

    region: Union[Unset, Region] = UNSET
    tax_jurisdiction_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict()

        tax_jurisdiction_id = self.tax_jurisdiction_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if tax_jurisdiction_id is not UNSET:
            field_dict["taxJurisdictionId"] = tax_jurisdiction_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _region = d.pop("region", UNSET)
        region: Union[Unset, Region]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        tax_jurisdiction_id = d.pop("taxJurisdictionId", UNSET)

        tax_jurisdiction = cls(
            region=region,
            tax_jurisdiction_id=tax_jurisdiction_id,
        )

        tax_jurisdiction.additional_properties = d
        return tax_jurisdiction

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

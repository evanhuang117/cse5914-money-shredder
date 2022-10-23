from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ship_to_region import ShipToRegion
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipToLocations")


@attr.s(auto_attribs=True)
class ShipToLocations:
    """The type that defines the fields that include and exclude geographic regions affecting where the item can be
    shipped. The seller defines these regions when listing the item.

        Attributes:
            region_excluded (Union[Unset, List[ShipToRegion]]): An array of containers that express the large geographical
                regions, countries, state/provinces, or special locations within a country where the seller is not willing to
                ship to.
            region_included (Union[Unset, List[ShipToRegion]]): An array of containers that express the large geographical
                regions, countries, or state/provinces within a country where the seller is willing to ship to. Prospective
                buyers must look at the shipping regions under this container, as well as the shipping regions that are under
                the <b>regionExcluded</b> to see where the seller is willing to ship items. Sellers can specify that they ship
                'Worldwide', but then add several large geographical regions (e.g. Asia, Oceania, Middle East) to the exclusion
                list, or sellers can specify that they ship to Europe and Africa, but then add several individual countries to
                the exclusion list.
    """

    region_excluded: Union[Unset, List[ShipToRegion]] = UNSET
    region_included: Union[Unset, List[ShipToRegion]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_excluded: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.region_excluded, Unset):
            region_excluded = []
            for region_excluded_item_data in self.region_excluded:
                region_excluded_item = region_excluded_item_data.to_dict()

                region_excluded.append(region_excluded_item)

        region_included: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.region_included, Unset):
            region_included = []
            for region_included_item_data in self.region_included:
                region_included_item = region_included_item_data.to_dict()

                region_included.append(region_included_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_excluded is not UNSET:
            field_dict["regionExcluded"] = region_excluded
        if region_included is not UNSET:
            field_dict["regionIncluded"] = region_included

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_excluded = []
        _region_excluded = d.pop("regionExcluded", UNSET)
        for region_excluded_item_data in _region_excluded or []:
            region_excluded_item = ShipToRegion.from_dict(region_excluded_item_data)

            region_excluded.append(region_excluded_item)

        region_included = []
        _region_included = d.pop("regionIncluded", UNSET)
        for region_included_item_data in _region_included or []:
            region_included_item = ShipToRegion.from_dict(region_included_item_data)

            region_included.append(region_included_item)

        ship_to_locations = cls(
            region_excluded=region_excluded,
            region_included=region_included,
        )

        ship_to_locations.additional_properties = d
        return ship_to_locations

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

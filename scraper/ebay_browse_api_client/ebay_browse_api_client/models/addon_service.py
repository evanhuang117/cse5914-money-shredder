from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.converted_amount import ConvertedAmount
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddonService")


@attr.s(auto_attribs=True)
class AddonService:
    """This container describes an add-on service that may be selected for an item or that may apply automatically. A
    charge may be associated with the add-on service.

        Attributes:
            selection (Union[Unset, str]): This field indicates whether the add-on service must be selected for the item.
                For implementation help, refer to <a href='https://developer.ebay.com/api-
                docs/buy/browse/types/gct:AddonServiceSelectionEnum'>eBay API documentation</a>
            service_fee (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can provide
                the amount in both the currency used on the eBay site where an item is being offered and the conversion of that
                value into another currency, if applicable.
            service_id (Union[Unset, str]): The ID number of the add-on service.
            service_type (Union[Unset, str]): The type of add-on service, such as AUTHENTICITY_GUARANTEE. For implementation
                help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:AddonServiceTypeEnum'>eBay API
                documentation</a>
    """

    selection: Union[Unset, str] = UNSET
    service_fee: Union[Unset, ConvertedAmount] = UNSET
    service_id: Union[Unset, str] = UNSET
    service_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        selection = self.selection
        service_fee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_fee, Unset):
            service_fee = self.service_fee.to_dict()

        service_id = self.service_id
        service_type = self.service_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selection is not UNSET:
            field_dict["selection"] = selection
        if service_fee is not UNSET:
            field_dict["serviceFee"] = service_fee
        if service_id is not UNSET:
            field_dict["serviceId"] = service_id
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        selection = d.pop("selection", UNSET)

        _service_fee = d.pop("serviceFee", UNSET)
        service_fee: Union[Unset, ConvertedAmount]
        if isinstance(_service_fee, Unset):
            service_fee = UNSET
        else:
            service_fee = ConvertedAmount.from_dict(_service_fee)

        service_id = d.pop("serviceId", UNSET)

        service_type = d.pop("serviceType", UNSET)

        addon_service = cls(
            selection=selection,
            service_fee=service_fee,
            service_id=service_id,
            service_type=service_type,
        )

        addon_service.additional_properties = d
        return addon_service

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

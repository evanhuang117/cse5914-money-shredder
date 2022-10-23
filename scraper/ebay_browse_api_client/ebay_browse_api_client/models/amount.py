from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Amount")


@attr.s(auto_attribs=True)
class Amount:
    """
    Attributes:
        currency (Union[Unset, str]): The list of valid currencies. Each <a href="https://www.iso.org/iso-4217-currency-
            codes.html " target="_blank">ISO 4217</a> currency code includes the currency name followed by the numeric
            value.<br /><br />For example, the Canadian Dollar code (CAD) would take the following form: <i>Canadian Dollar,
            124</i>. For implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/ba:CurrencyCodeEnum'>eBay API documentation</a>
        value (Union[Unset, str]): The value of the discounted amount.
    """

    currency: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        value = d.pop("value", UNSET)

        amount = cls(
            currency=currency,
            value=value,
        )

        amount.additional_properties = d
        return amount

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

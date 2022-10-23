from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddCartItemInput")


@attr.s(auto_attribs=True)
class AddCartItemInput:
    """The type that defines the fields for the <b>addItems</b> request.

    Attributes:
        item_id (Union[Unset, str]): The eBay RESTful identifier of the item you want added to the cart. <br /><br />
            <b>RESTful Item ID Format: </b><code>v1</code>|<code><i>#</i></code>|<code><i>#</i></code> <br /><b> For
            example: </b> <br /><code>v1|2**********2|0</code> <br /><code>v1|1**********2|4**********2</code> <br /><br
            />For more information about item ID for RESTful APIs, see the <a href="/api-docs/buy/static/api-
            browse.html#Legacy">Legacy API compatibility</a> section of the <i>Buy APIs Overview</i>.<br /><br /><b> Maximum
            number of items in a cart: </b> 100
        quantity (Union[Unset, int]): The number of this item the buyer wants to purchase. If this value is greater than
            the number available, the service will change this value to the number available. If this happens, a warning is
            returned.<br /><br /><b> Maximum: </b> <i>number available</i>
    """

    item_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_id = self.item_id
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        item_id = d.pop("itemId", UNSET)

        quantity = d.pop("quantity", UNSET)

        add_cart_item_input = cls(
            item_id=item_id,
            quantity=quantity,
        )

        add_cart_item_input.additional_properties = d
        return add_cart_item_input

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

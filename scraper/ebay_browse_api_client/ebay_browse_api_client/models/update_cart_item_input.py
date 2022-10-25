from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCartItemInput")


@attr.s(auto_attribs=True)
class UpdateCartItemInput:
    """The type that defines the fields for the <b>updateQuantity</b> request.

    Attributes:
        cart_item_id (Union[Unset, str]): The identifier of the item in the cart to be updated. This ID is generated
            when the item was added to the cart.
        quantity (Union[Unset, int]): The new quantity for the item that is being updated.
    """

    cart_item_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cart_item_id = self.cart_item_id
        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cart_item_id is not UNSET:
            field_dict["cartItemId"] = cart_item_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cart_item_id = d.pop("cartItemId", UNSET)

        quantity = d.pop("quantity", UNSET)

        update_cart_item_input = cls(
            cart_item_id=cart_item_id,
            quantity=quantity,
        )

        update_cart_item_input.additional_properties = d
        return update_cart_item_input

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

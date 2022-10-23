from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.amount import Amount
from ..models.cart_item import CartItem
from ..models.error import Error
from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoteShopcartResponse")


@attr.s(auto_attribs=True)
class RemoteShopcartResponse:
    """The type that defines the fields and containers for the member's eBay cart information.

    Attributes:
        cart_items (Union[Unset, List[CartItem]]): An array of the items in the member's eBay cart.
        cart_subtotal (Union[Unset, Amount]):
        cart_web_url (Union[Unset, str]): The URL of the member's eBay cart.
        unavailable_cart_items (Union[Unset, List[CartItem]]): An array of items in the cart that are unavailable. This
            can be for a variety of reasons such as, when the listing has ended or the item is out of stock. Because a cart
            never expires, these items will remain in the cart until they are removed.
        warnings (Union[Unset, List[Error]]): An array of warning messages. These type of errors do not prevent the call
            from executing but should be checked.
    """

    cart_items: Union[Unset, List[CartItem]] = UNSET
    cart_subtotal: Union[Unset, Amount] = UNSET
    cart_web_url: Union[Unset, str] = UNSET
    unavailable_cart_items: Union[Unset, List[CartItem]] = UNSET
    warnings: Union[Unset, List[Error]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cart_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cart_items, Unset):
            cart_items = []
            for cart_items_item_data in self.cart_items:
                cart_items_item = cart_items_item_data.to_dict()

                cart_items.append(cart_items_item)

        cart_subtotal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cart_subtotal, Unset):
            cart_subtotal = self.cart_subtotal.to_dict()

        cart_web_url = self.cart_web_url
        unavailable_cart_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unavailable_cart_items, Unset):
            unavailable_cart_items = []
            for unavailable_cart_items_item_data in self.unavailable_cart_items:
                unavailable_cart_items_item = unavailable_cart_items_item_data.to_dict()

                unavailable_cart_items.append(unavailable_cart_items_item)

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()

                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cart_items is not UNSET:
            field_dict["cartItems"] = cart_items
        if cart_subtotal is not UNSET:
            field_dict["cartSubtotal"] = cart_subtotal
        if cart_web_url is not UNSET:
            field_dict["cartWebUrl"] = cart_web_url
        if unavailable_cart_items is not UNSET:
            field_dict["unavailableCartItems"] = unavailable_cart_items
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cart_items = []
        _cart_items = d.pop("cartItems", UNSET)
        for cart_items_item_data in _cart_items or []:
            cart_items_item = CartItem.from_dict(cart_items_item_data)

            cart_items.append(cart_items_item)

        _cart_subtotal = d.pop("cartSubtotal", UNSET)
        cart_subtotal: Union[Unset, Amount]
        if isinstance(_cart_subtotal, Unset):
            cart_subtotal = UNSET
        else:
            cart_subtotal = Amount.from_dict(_cart_subtotal)

        cart_web_url = d.pop("cartWebUrl", UNSET)

        unavailable_cart_items = []
        _unavailable_cart_items = d.pop("unavailableCartItems", UNSET)
        for unavailable_cart_items_item_data in _unavailable_cart_items or []:
            unavailable_cart_items_item = CartItem.from_dict(unavailable_cart_items_item_data)

            unavailable_cart_items.append(unavailable_cart_items_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        remote_shopcart_response = cls(
            cart_items=cart_items,
            cart_subtotal=cart_subtotal,
            cart_web_url=cart_web_url,
            unavailable_cart_items=unavailable_cart_items,
            warnings=warnings,
        )

        remote_shopcart_response.additional_properties = d
        return remote_shopcart_response

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

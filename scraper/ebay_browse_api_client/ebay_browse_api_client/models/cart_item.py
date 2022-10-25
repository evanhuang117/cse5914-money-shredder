from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.amount import Amount
from ..models.image import Image
from ..models.price import Price
from ..types import UNSET, Unset

T = TypeVar("T", bound="CartItem")


@attr.s(auto_attribs=True)
class CartItem:
    """The type that defines the fields for the individual items in a cart.

    Attributes:
        cart_item_id (Union[Unset, str]): The identifier for the item being added to the cart. This is generated when
            the item is added to the cart.
        cart_item_subtotal (Union[Unset, Amount]):
        image (Union[Unset, Image]): Type the defines the details of an image, such as size and image URL. Currently,
            only <b> imageUrl</b> is  populated. The <b> height</b> and <b> width</b> were added for future use.
        item_id (Union[Unset, str]): The RESTful identifier of the item. This identifier is generated when the item was
            listed. <br /><br /> <b>RESTful Item ID Format: </b><code>v1</code>|<code><i>#</i></code>|<code><i>#</i></code>
            <br /><b> For example: </b><br /> <code>v1|2**********2|0</code> <br /><code>v1|1**********2|4**********2</code>
        item_web_url (Union[Unset, str]): The URL of the eBay view item page for the item.
        price (Union[Unset, Price]): The type that defines the fields for the monetary value and currency of the price
            of the item.
        quantity (Union[Unset, int]): The number of this item the buyer wants to purchase.
        title (Union[Unset, str]): The title of the item. This can be written by the seller or come from the eBay
            product catalog.
    """

    cart_item_id: Union[Unset, str] = UNSET
    cart_item_subtotal: Union[Unset, Amount] = UNSET
    image: Union[Unset, Image] = UNSET
    item_id: Union[Unset, str] = UNSET
    item_web_url: Union[Unset, str] = UNSET
    price: Union[Unset, Price] = UNSET
    quantity: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cart_item_id = self.cart_item_id
        cart_item_subtotal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cart_item_subtotal, Unset):
            cart_item_subtotal = self.cart_item_subtotal.to_dict()

        image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        item_id = self.item_id
        item_web_url = self.item_web_url
        price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        quantity = self.quantity
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cart_item_id is not UNSET:
            field_dict["cartItemId"] = cart_item_id
        if cart_item_subtotal is not UNSET:
            field_dict["cartItemSubtotal"] = cart_item_subtotal
        if image is not UNSET:
            field_dict["image"] = image
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if item_web_url is not UNSET:
            field_dict["itemWebUrl"] = item_web_url
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cart_item_id = d.pop("cartItemId", UNSET)

        _cart_item_subtotal = d.pop("cartItemSubtotal", UNSET)
        cart_item_subtotal: Union[Unset, Amount]
        if isinstance(_cart_item_subtotal, Unset):
            cart_item_subtotal = UNSET
        else:
            cart_item_subtotal = Amount.from_dict(_cart_item_subtotal)

        _image = d.pop("image", UNSET)
        image: Union[Unset, Image]
        if isinstance(_image, Unset):
            image = UNSET
        else:
            image = Image.from_dict(_image)

        item_id = d.pop("itemId", UNSET)

        item_web_url = d.pop("itemWebUrl", UNSET)

        _price = d.pop("price", UNSET)
        price: Union[Unset, Price]
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)

        quantity = d.pop("quantity", UNSET)

        title = d.pop("title", UNSET)

        cart_item = cls(
            cart_item_id=cart_item_id,
            cart_item_subtotal=cart_item_subtotal,
            image=image,
            item_id=item_id,
            item_web_url=item_web_url,
            price=price,
            quantity=quantity,
            title=title,
        )

        cart_item.additional_properties = d
        return cart_item

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

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.image import Image
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethodBrand")


@attr.s(auto_attribs=True)
class PaymentMethodBrand:
    """
    Attributes:
        payment_method_brand_type (Union[Unset, str]): The payment method brand, such as Visa or PayPal. For
            implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/gct:PaymentMethodBrandEnum'>eBay API documentation</a>
        logo_image (Union[Unset, Image]): Type the defines the details of an image, such as size and image URL.
            Currently,  only <b> imageUrl</b> is  populated. The <b> height</b> and <b> width</b> were added for future use.
    """

    payment_method_brand_type: Union[Unset, str] = UNSET
    logo_image: Union[Unset, Image] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_method_brand_type = self.payment_method_brand_type
        logo_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.logo_image, Unset):
            logo_image = self.logo_image.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_method_brand_type is not UNSET:
            field_dict["paymentMethodBrandType"] = payment_method_brand_type
        if logo_image is not UNSET:
            field_dict["logoImage"] = logo_image

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        payment_method_brand_type = d.pop("paymentMethodBrandType", UNSET)

        _logo_image = d.pop("logoImage", UNSET)
        logo_image: Union[Unset, Image]
        if isinstance(_logo_image, Unset):
            logo_image = UNSET
        else:
            logo_image = Image.from_dict(_logo_image)

        payment_method_brand = cls(
            payment_method_brand_type=payment_method_brand_type,
            logo_image=logo_image,
        )

        payment_method_brand.additional_properties = d
        return payment_method_brand

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

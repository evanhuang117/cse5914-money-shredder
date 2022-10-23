from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Image")


@attr.s(auto_attribs=True)
class Image:
    """Type the defines the details of an image, such as size and image URL. Currently,  only <b> imageUrl</b> is
    populated. The <b> height</b> and <b> width</b> were added for future use.

        Attributes:
            height (Union[Unset, int]): Reserved for future use.
            image_url (Union[Unset, str]): The URL of the image.
            width (Union[Unset, int]): Reserved for future use.
    """

    height: Union[Unset, int] = UNSET
    image_url: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        height = self.height
        image_url = self.image_url
        width = self.width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        height = d.pop("height", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        width = d.pop("width", UNSET)

        image = cls(
            height=height,
            image_url=image_url,
            width=width,
        )

        image.additional_properties = d
        return image

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

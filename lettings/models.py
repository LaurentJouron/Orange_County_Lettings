from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing an address.

    This class defines an address model with fields for the number, street,
    city, state, zip code, and country ISO code. The number field is a positive
    integer with a maximum value of 9999. The street, city, state, and country
    ISO code fields are character fields with specified maximum lengths.
    The zip code field is a positive integer with a maximum value of 99999.

    Returns:
        A string representation of the address.

    Examples:
        >>> address = Address(number=123, street="Main St", city="City",
        state="CA", zip_code=12345, country_iso_code="USA")
        >>> str_representation = str(address)
    """

    class Meta:
        verbose_name = "Adress"
        verbose_name_plural = "Adresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)]
    )
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Model representing a letting.

    This class defines a letting model with a title and an address. The title
    is a character field with a maximum length of 256 characters. The address
    is a one-to-one relationship with the Address model.

    Returns:
        A string representation of the letting.

    Examples:
        >>> letting = Letting(title="Sample Letting", address=address_instance)
        >>> str_representation = str(letting)
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

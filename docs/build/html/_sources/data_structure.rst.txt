.. _data_structure:

**Data structure**
==================

*******
Address
*******

* verbose_name = "Address"
* verbose_name_plural = "Addresses"

.. csv-table::
   :header: "number", "street", "city", "state", "zip_code", "country_iso_code"

   "PositiveIntegerField", "CharField", "CharField", "CharField", "PositiveIntegerField", "CharField"
   "validators=[MaxValueValidator(9999)]", "max_length=64", "max_length=64", "max_length=2", "validators=[MaxValueValidator(99999)]", "max_length=3"
   "", "", "", "validators=[MinLengthValidator(2)]", "", "validators=[MinLengthValidator(3)]"


********
Lettings
********
.. csv-table::
   :header: "title", "address"

   "CharField", "OneToOneField"
   "max_length=256", "Address"
   "", "on_delete=models.CASCADE"

********
Profile
********
.. csv-table::
   :header: "user", "favorite_city"

   "User", "CharField"
   "on_delete=models.CASCADE", "max_length=64"
   "", "blank=True"


******
Schema
******

.. _ma_figure:

.. figure:: _static/database_structure.png
   :height: 400
   :width: 700
   :scale: 80
   :align: center
   :alt: Database structure

   :download:`Download <_static/database_structure.png>`
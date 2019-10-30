=======
History
=======

1.5.1 (2019-10-31)
------------------

- Fix bug where new API field would raise a TypeError
- Update :code:`pytest` to 5.2.2
- Update :code:`sphinx` to 2.2.1


1.5.0 (2019-10-19)
------------------

- Added support to group_id in models
- Update :code:`pytest` to 5.2.1
- Update :code:`pytest-cov` to 2.8.1


1.4.1 (2019-10-04)
------------------

- Add fix for edge case where decoded locations are empty but still given


1.4.0 (2019-10-04)
------------------

- Update pytest from 5.1.2 to 5.2.0
- Add support for decoded locations


1.3.4 + 1.3.5 (2019-09-19)
--------------------------

- Lift :code:`jsonschema` dependency even more for broad support


1.3.3 (2019-09-15)
------------------

- Update twine from 1.13.0 to 1.14.0
- Take over :code:`jsonschema` dependency to support web3py


1.3.2 (2019-09-06)
------------------

- Update pytest from 5.1.1 to 5.1.2
- Add models to fetch analysis input data


1.3.1 (2019-08-30)
------------------

- Add info field to analysis status model


1.3.0 (2019-08-29)
------------------

- Allow null values in submission request and issues response models


1.2.0 (2019-08-29)
------------------

- Added models for source map representation (including source map decompression)


1.1.0 (2019-08-27)
------------------

- Removed the minimum size limit for a detected issue report list
- Added an :code:`as_list` option to the detected issue response model to support non-object input


1.0.0 (2019-08-26)
------------------

- Added all models originally in PythX
- Extended models with :code:`BaseModel` class
- Make issue reports and various submodels JSON serializable
- Added documentation to readthedocs.io
- Added CI with Travis
- Added coverage metrics with codecov
- Added packaging pipeline to PyPI

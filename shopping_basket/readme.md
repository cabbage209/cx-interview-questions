## Documentation

Please put your documentation in this file.

My shopping basket implementation

Offers:
Crabs buy 3 get 1 free
Fish 20% off


4 classes:
Basket:
This class holds the mutable list of items within the basket.
+sub_total, discount and total member variables

Item: 
This class is used to define catalogue items with their unique price and quantity.

Pricer:
This class handles the sum of the total via sub_total - discount.
It also applies items discount via offers

Bonus:
This was created to attempt the bonus question.


To run pytest outside the venv:
pipenv run pytest

To run flake8 outside the venv:
pipenv run flake8

To run black inside the venv:
black .

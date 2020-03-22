# covid-19-analysis

Implementations to visualize dataset of COVID-19 cases and deaths

## Dependecies

This project was built with Python3.7 and have the following dependencies:

| Dependency | Version |
| ---------- | ------- |
| Numpy      | 1.18.2  |
| Pandas     | 1.0.3   |
| Jupyter*   | 1.0.0   |

- **\***: The jupyter package is optional, but will be installed along the other packages. You can use the `covid` module "outside the box".

## How to

### Install

To install the project dependencies, you'll need [`pipvenv`](https://github.com/pypa/pipenv). To install the packages:

```bash
pipenv install
```

### Use

If you want to use the class inside a notebook, run the jupyter inside de virtual environment:

```bash
pipenv run jupyter notebook
```

## Module

The `covid` module contains a class named `COVID`. The class generates a DataFrame from a csv that can be found [here](https://covid.ourworldindata.org/data/ecdc/full_data.csv).

### `COVID`

The class `COVID` counts with a few methods to generate line charts of the data, and they're listed below:

#### `by_location(location1,location2,...)`

Returns all the data for the given locations.

##### Arguments

- `location<n>`: Multiple location, any of `("World","Afghanistan","Brazil",...)`

##### Example

> [In: 1] dataset.by_location("Brazil")
>  
> [Out: 2]
>
> ![by_location() example](https://i.imgur.com/KXdBial.png)

#### `from_date(date,location1,location2,...)`

Returns all the data for the given locations.

##### Arguments

- date: Date in format `YYYY-MM-DD`
- `location<n>`: Multiple locations, any of `("World","Afghanistan","Brazil",...)`

##### Example

> [In: 1] dataset.from_date("2020-03-11","Brazil")
>
> [Out: 2]
>
> ![from_date() example](https://i.imgur.com/BuP2rMd.png)

#### `plot_total_deaths(location1,location2,...)`

Plot a line chart with the total deaths with the given locations

##### Arguments 

- `location<n>`: Multiple locations, any of `("World","Afghanistan","Brazil",...)`

##### Example

> [In: 1] dataset.plot_total_deaths("World","Italy","China")
>  
> [Out: 2]
>
> ![plot_total_deaths() example](https://i.imgur.com/TiMIGhM.png)

#### `plot_total_cases(location1,location2,...)`

Plot a line chart with the total cases with the given locations

##### Arguments 

- `location<n>`: Multiple locations, any of `("World","Afghanistan","Brazil",...)`

##### Example

> [In: 1] dataset.plot_total_cases("China","Italy","World")
>  
> [Out: 2]
>
> ![plot_total_cases() example](https://i.imgur.com/yELygkx.png)

## References

- Data: The dataset was extracted from the [Our World In Data - Coronavirus Source Data](https://ourworldindata.org/coronavirus-source-data) website.
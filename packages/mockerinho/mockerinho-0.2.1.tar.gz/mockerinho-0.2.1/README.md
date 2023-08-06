# Mockerinho

[![Build](https://github.com/mockerinho/mockerinho/actions/workflows/build.yml/badge.svg)](https://github.com/mockerinho/mockerinho/actions/workflows/build.yml)
[![GitLicense](https://gitlicense.com/badge/mockerinho/mockerinho)](https://gitlicense.com/license/mockerinho/mockerinho)

![Mockerinho banner](https://github.com/mockerinho/mockerinho/raw/main/docs/images/banner.jpeg)

A tool designed to simulate HTTP-based APIs for development and testing purposes.

## Installation

You can install this package using pip

```
pip install mockerinho
```

## Usage

Run the utility and specify simulations configurations directory (host and port are optional)

```
mockerinho -H 127.0.0.1 \
           -p 3000 \
           -D data/examples/simulations
```

Send request to the simulator

```
curl -i \
     -X POST http://127.0.0.1:3000/users \
     -H 'Content-Type: application/json' \
     -d '{"name": "Alex"}'
```

Get response from the simulator

```
HTTP/1.1 201 CREATED
Content-Type: application/json
Content-Length: 18
Connection: Keep-Alive

{ "name": "Alex" }
```

For more information about simulation configuration, see the [simulation configuration reference](docs/simulation_configuration.md).

## Author

[Mikhail Eremeev](mailto:meremeev@sfedu.ru)

## License

[MIT](https://opensource.org/licenses/MIT)

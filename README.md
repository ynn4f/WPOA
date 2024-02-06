# Webpage Last Modified Timestamp

Webpage Last Modified Timestamp is a Python script that retrieves the last modified timestamp of a webpage. It can extract the timestamp from the `last-modified` header or from a meta tag named `date` in the HTML of the webpage.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:

```
pip install requests beautifulsoup4
```

3. Clone the repository to your local machine.
4. Navigate to the directory containing the script.
5. Run the script using the following command:

```sh
python script.py -s <URL>
```

Replace `<URL>` with the URL of the webpage you want to retrieve the last modified timestamp for.

## Options

- `-s, --url`: Specifies the URL of the webpage.

## Example

```sh
python script.py -s https://example.com
```

This will retrieve the last modified timestamp of the webpage `https://example.com` and display it in a human-readable format.

## License

This project is not licensed. Feel free to use it, modify it, and distribute it as you wish.

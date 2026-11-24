# Arabic Search Fold

Generate a normalized search column for Arabic names while preserving their original spelling.

## Run

From this folder with Python 3.9 or later:

```sh
python main.py contacts.csv name searchable.csv
```

For a CSV with a `name` column, the new `search_key` folds alef variants, common marks, tatweel, and alef maqsura. Different names can share a search key. Use the result for lookup suggestions. Choose a new output filename.

## Limitations

Distinct names can share a search key. Use it for lookup rather than identity matching.

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and test commands, and the [changelog](CHANGELOG.md) for project history.

## License

[MIT License](LICENSE). Copyright (c) 2026 arabic-search-fold contributors.

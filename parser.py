import csv


INPUT_FILENAME = 'x.txt'
OUTPUT_FILENAME = 'speeds.csv'


def parse_input_file(input_filename):
    with open(input_filename) as input_file:
        rows = []
        row_data = {'time': ''}
        for line in input_file:
            trimmed_line = line.strip()
            if not trimmed_line:
                continue
            parts = trimmed_line.split(':', maxsplit=1)
            key = parts[0].lower()

            if key.startswith('logged time'):
                parts = trimmed_line.split('=')
                row_data['time'] = parts[1].strip()
            elif len(parts) > 1:
                row_data[key] = parts[1].strip()

            if key == 'result url':
                rows.append(row_data)
                row_data = {'time': ''}

        return rows


def write_output_file(output_filename, rows):
    with open(output_filename, 'w', newline='') as output_file:
        field_names = rows[0].keys()
        writer = csv.DictWriter(output_file, field_names, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(rows)


def main():
    rows = parse_input_file(INPUT_FILENAME)
    if rows:
        write_output_file(OUTPUT_FILENAME, rows)


if __name__ == "__main__":
    main()

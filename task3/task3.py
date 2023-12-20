import json
import copy
import sys

def update_values(test_structure, test_results):
    if 'id' in test_structure:
        test_id = test_structure['id']
        for result in test_results:
            if result['id'] == test_id:
                test_structure['value'] = result['value']
                break

    if 'values' in test_structure:
        for subtest in test_structure['values']:
            update_values(subtest, test_results)

def main(tests_file, values_file, output_file):
    with open(tests_file, 'r') as f:
        tests_data = json.load(f)

    with open(values_file, 'r') as f:
        test_results = json.load(f)['values']

    tests_data_copy = copy.deepcopy(tests_data)

    for test in tests_data_copy.get('tests', []):
        update_values(test, test_results)

    with open(output_file, 'w') as f:
        json.dump(tests_data_copy, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error")
    else:
        tests_file = sys.argv[1]
        values_file = sys.argv[2]
        output_file = 'report.json'

        main(tests_file, values_file, output_file)


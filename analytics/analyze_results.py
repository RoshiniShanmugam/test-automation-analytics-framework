import xml.etree.ElementTree as ET
import pandas as pd
import os

def parse_robot_output(xml_file):
    if not os.path.exists(xml_file):
        print(f"Error: {xml_file} not found!")
        return None

    tree = ET.parse(xml_file)
    root = tree.getroot()

    test_data = []

    # Iterate through each test case in the XML report
    for test in root.iter('test'):
        test_name = test.get('name')
        status_elem = test.find('status')
        
        status = status_elem.get('status') if status_elem is not None else 'UNKNOWN'
        start_time = status_elem.get('starttime') if status_elem is not None else 'N/A'
        end_time = status_elem.get('endtime') if status_elem is not None else 'N/A'

        test_data.append({
            'Test Case Name': test_name,
            'Status': status,
            'Start Time': start_time,
            'End Time': end_time
        })

    return pd.DataFrame(test_data)

def generate_analytics_summary(df):
    total_tests = len(df)
    passed_tests = len(df[df['Status'] == 'PASS'])
    failed_tests = len(df[df['Status'] == 'FAIL'])
    pass_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

    print("\n==========================================")
    print("      TEST AUTOMATION ANALYTICS REPORT    ")
    print("==========================================")
    print(f"Total Tests Executed : {total_tests}")
    print(f"Passed Tests         : {passed_tests}")
    print(f"Failed Tests         : {failed_tests}")
    print(f"Pass Rate            : {pass_rate:.2f}%")
    print("==========================================\n")

    # Export structured report to CSV
    output_csv = os.path.join("results", "analytics_summary.csv")
    df.to_csv(output_csv, index=False)
    print(f"[SUCCESS] Detailed test execution report saved to: {output_csv}")

if __name__ == "__main__":
    xml_path = os.path.join("results", "output.xml")
    df_results = parse_robot_output(xml_path)
    
    if df_results is not None:
        generate_analytics_summary(df_results)
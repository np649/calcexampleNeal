import glob
import pathlib
import os
import pandas as pd
import time

from calculator.calculator import Calculator

def process(files):
    for file in files:
        basename = os.path.basename(file)
        # print(basename)
        if basename == "addition.csv":
            print("add")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.add_number(row['Value_1'], row['Value_2'])
                with open("results/results.txt", "a") as fp:
                    fp.write(f"Time: {time.time()}, File: {file}, "
                             f"Record Number: {index}, " f"Operation: add, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["Result"] = results_arr
            with open(f"output_csvs/{basename}", "w") as fp:
                df.to_csv(fp)
                # to remove add os.remove(file)
        if basename == "subtraction.csv":
            print("sub")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.subtract_number(row['Value_1'], row['Value_2'])
                with open("results/results.txt", "a") as fp:
                    fp.write(
                        f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                        f"Operation: subtract, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["Result"] = results_arr
            with open(f"output_csvs/{basename}", "w") as fp:
                df.to_csv(fp)
        if basename == "multiplication.csv":
            print("multiply")
            df = pd.read_csv(file)
            results_arr = []
            for index, row in df.iterrows():
                temp = Calculator.multiply_numbers(row['Value_1'], row['Value_2'])
                with open("results/results.txt", "a") as fp:
                    fp.write(
                        f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                        f"Operation: multiply, Result: {temp}\n")
                    fp.close()
                results_arr.append(temp)
            df["Result"] = results_arr
            with open(f"output_csvs/{basename}", "w") as fp:
                df.to_csv(fp)
        if basename == "division.csv":
            print("division")
            df = pd.read_csv(file)
            results_arr = []
            # Loop Through records
            for index, row in df.iterrows():
                # Catch divide by 0 error
                if row['Value_2'] == 0:
                    with open("results/exceptions.txt", "a") as fp:
                        fp.write(f"File: {file}, Record Number: {index}\n")
                        fp.close()
                    results_arr.append("NaN")
                else:
                    # Operation
                    temp = Calculator.divide_numbers(row['Value_1'], row['Value_2'])
                    # Write to log
                    with open("results/results.txt", "a") as fp:
                        fp.write(f"Time: {time.time()}, File: {file}, Record Number: {index}, "
                                 f"Operation: divide, Result: {temp}\n")
                        fp.close()
                    results_arr.append(temp)

            # Make output CSVs
            df["Result"] = results_arr
            with open(f"output_csvs/{basename}", "w") as fp:
                df.to_csv(fp)

    return 0

def main():
    path = pathlib.Path(__file__).parent / "input_csvs"
    # print ("path: " + str(path))
    files = glob.glob(str(path) + "/*")
    # print(files)
    files_len = len(files)
    while True:
        if files_len != 0:
            print("Processing...")
            done = process(files)
            files_len = done
        else:
            print("Running...", end="\r")

        
    return True

main()

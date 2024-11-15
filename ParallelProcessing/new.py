import pandas as pd
job_postings = pd.read_csv("DataEngineer.csv")
num_rows = job_postings.shape[0]
num_cols = job_postings.shape[1]

job_postings["Job Description"] = job_postings["Job Description"].str.lower()
frequency = {}
frequency["postgres"] = job_postings["Job Description"].str.count("postgres").sum()
frequency["sql"] = job_postings["Job Description"].str.count("sql").sum()

print(frequency)

skills = pd.read_csv("Skills.csv")

frequency = {}
for skill_name in skills["Name"]:
    frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    
print(frequency["programming"])

import time

#frequency = {}
#for skill_name in skills["Name"]:
#    frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency


start = time.time()
count_skills(job_postings, skills)
end = time.time()
runtime = end - start

import math
def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows / num_chunks)
    return [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]

skill_chunks = make_chunks(skills, 8)

import concurrent.futures

def increment(value):
    return value + 1

values = [1, 2, 3, 4, 5, 6, 7, 8]

# Add code here
with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(increment, value) for value in values]

results = [future.result() for future in futures]


import concurrent.futures
skill_chunks = make_chunks(skills, 8)

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]

results = [future.result() for future in futures]
print(results[0])

merged_results = {}
for result in results:
    merged_results.update(result)

def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency

def count_skills_parallel(job_postings, skills, num_processes=4):
    # Calculate results using paralleld processing
    skill_chunks = make_chunks(skills, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]
    results = [future.result() for future in futures]
    # Merge results
    merged_results = {}
    for result in results:
        merged_results.update(result)
    return merged_results

import time

# Measure execution times here
start = time.time()
count_skills(job_postings, skills)
end = time.time()
time_normal = end - start

start = time.time()
count_skills_parallel(job_postings, skills)
end = time.time()
time_parallel = end - start

print(time_normal / time_parallel)


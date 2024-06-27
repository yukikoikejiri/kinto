# Report for Assignment 1

> [!NOTE]
> As each member has a different laptop version, the command line might vary slightly.

## Project chosen

**Name:** Kinto \
**URL:** https://github.com/Kinto/kinto \
**Number of lines of code and the tool used to count it:** 25,608 LOC (96.1% written in Python) counted by Lizard \
**Programming language:** Python

## Coverage measurement

### Existing tool

**Tool:** Coverage.py \
**Execution:**
- Installed the tool by command ```pip install coverage```
- Change the directory to the project path; _kinto-main_ folder
- Execute the coverage with command ```python3 -m coverage run -m unittest discover```
- Generate report as html file by using command ```python3 -m coverage report```
 and ```python3 -m coverage html```

**Result of Coverage report:** 87%
> Link to the [screenshot](https://drive.google.com/file/d/1zhVf29ru1ji9dSbwJ45Req72xLHChiUe/view?usp=drive_link) \
> Link to the [html files](https://drive.google.com/file/d/1_RrgHzZo1sa60eLcNcWoIA7hAc_Az6AF/view?usp=sharing)

### Your own coverage tool

**Name:** Charanan Mahakijpalach \
Comparing code: https://github.com/Kinto/kinto/compare/main...yukikoikejiri:kinto:A1_Mun

**Function 1:** ```watch_execution_time(self, obj, prefix="", classname=None)``` \
Path: _kinto/core/statsd.py_ \
**Instrumented code:** https://github.com/Kinto/kinto/commit/240233fa86cbe85b6229fc67b61a396568abde87 \
Command to run the instrumentation: ```coverage run -m unittest tests/core/test_statsd.py``` \
**Result:**

<img width="464" alt="Mun_func1" src="https://github.com/yukikoikejiri/kinto/assets/113595508/29a7b25e-2043-43a5-8f4f-af83a63b6424">

\
**Function 2:** ```load_from_config(config)``` \
Path: _kinto/core/statsd.py_ \
**Instrumented code:** https://github.com/Kinto/kinto/commit/355f2d1ecf8bcf88d3403b8736e21968687e6871  
Command to run the instrumentation: ```coverage run -m unittest tests/core/test_statsd.py``` \
**Result:**

<img width="465" alt="Mun_func2" src="https://github.com/yukikoikejiri/kinto/assets/113595508/8bf54fba-d7a0-4250-8f9e-6d7174aebbf0">


\
\
**Name:** Cindy-Virginia Enekwemchi \
Comparing code: https://github.com/Kinto/kinto/compare/main...yukikoikejiri:kinto:A1_Cindy 

**Function 1:** ```statsd_count(request, count_key)``` \
Path: _kinto/core/statsd.py_ \
**Instrumented code:** https://github.com/Kinto/kinto/commit/848f7deec2b656c3c236de1cc80af06391da7fec \
Command to run the instrumentation: ```coverage run -m unittest tests/core/test_statsd.py``` \
**Result:**

<img width="467" alt="Cindy_func1" src="https://github.com/yukikoikejiri/kinto/assets/113595508/38759476-2ea6-4bd4-b3f3-b08ab80e8761">

\
**Function 2:** ```count(self, key, count=1, unique=None)``` \
Path: _kinto/core/statsd.py_ \
**Instrumented code:** https://github.com/Kinto/kinto/commit/848f7deec2b656c3c236de1cc80af06391da7fec \
Command to run instrumentation: ```coverage run -m unittest tests/core/test_statsd.py``` \
**Result:**

<img width="466" alt="Cindy_func2" src="https://github.com/yukikoikejiri/kinto/assets/113595508/0e2530ed-2f4a-4e98-a8ae-f3f3c33cf6cc">


\
\
**Name:** Lisa Lipkovich \
Comparing code: https://github.com/Kinto/kinto/compare/main...yukikoikejiri:kinto:A1_Lisa 

**Function 1:** ```create_schema(self, dry_run)``` \
Path: _kinto/core/storage/postgresql/migrator.py_ \
**Instrumented code:** https://github.com/Kinto/kinto/commit/5620c28ce4d0ee5d6c1c48795029a1fe429439bc \
Command to run instrumentation: ```coverage run -m unittest tests/core/test_storage_migrations.py``` \
**Result:**

<img width="465" alt="Lisa_func1" src="https://github.com/yukikoikejiri/kinto/assets/113595508/e3f811b3-e322-480f-b553-33c9a73fd35c">

\
**Function 2:** ```__call__(self, request, *args, **kwargs)``` \
Path: _kinto/core/decorators.py_ \
**Instrumented code:** https://github.com/Kinto/kinto/commit/1fe56d8f87da5e69bbdfcb17daa3f31ee920c410 \
Command to run instrumentation: ```coverage run -m unittest tests/core/test_decorators.py``` \
**Result:**

<img width="464" alt="Lisa_func2" src="https://github.com/yukikoikejiri/kinto/assets/113595508/d7d35ef7-a4d6-48dc-8717-0d894f64aa02">


\
\
**Name:** Yukiko Ikejiri \
Comparing code: https://github.com/Kinto/kinto/compare/main...yukikoikejiri:kinto:A1_Yukiko

**Function 1:** ```Storage._check_database_timezone(self)``` \
Path: _kinto/core/storage/postgresql/__init__.py_ \
**Instrumented code:** https://github.com/Kinto/kinto/commit/1ca09fa770077cf9792b371a8798c1800891efc5 \
Command to run the instrumentation: ```python3 -m coverage run -m unittest tests/core/test_storage.py``` \
**Result:**

<img width="465" alt="Yukiko_func1" src="https://github.com/yukikoikejiri/kinto/assets/113595508/0fc6ed25-09cc-44de-bfc1-723a551441c5">

\
**Function 2:** ```Storage._check_database_encoding(self)``` \
Path: _kinto/core/storage/postgresql/__init__.py_ \
**Instrumented code:** https://github.com/Kinto/kinto/commit/17f077ddf8f7e761be41b99256b2a0197a4060ec \
Command to run the instrumentation: ```python3 -m coverage run -m unittest tests/core/test_storage.py``` \
**Result:**

<img width="466" alt="Yukiko_func2" src="https://github.com/yukikoikejiri/kinto/assets/113595508/8df1080d-8253-4117-960a-6a7c16c00540">


## Coverage improvement

### Individual tests

**Name:** Charanan Mahakijpalach \
Comparing code: https://github.com/Kinto/kinto/compare/main...yukikoikejiri:kinto:A1_Mun

**Test 1** - for function ```watch_execution_time(self, obj, prefix="", classname=None)``` \
**New test code:** https://github.com/Kinto/kinto/commit/62b3516367ff811757795fba9519d27290ad16f9 \
**Result of old coverage:**

<img width="464" alt="Mun_func1" src="https://github.com/yukikoikejiri/kinto/assets/113595508/29a7b25e-2043-43a5-8f4f-af83a63b6424">

**Result of new coverage:**

<img width="466" alt="Mun_func1_new" src="https://github.com/yukikoikejiri/kinto/assets/113595508/0188332c-eb57-4249-aa83-e675df774b1e">

**Statement and reason of the coverage improvement:**
> The coverage from the instrumentation increased from 0% to 100%. 
- The old coverage report showed that none of the branches in the function were covered because the existing test cases only test the function when the user has a _statsd_ module installed; therefore, the existing test cases were skipped. 
- A new test case, ```test_watch_execution_time_decorates_public_method(self, module_mock)```, has been added to ensure the test file also covers the function in the scenario where no _statsd_ module is installed.
- This test case hits branch 1, which contains a for-statement with condition ```name in members```. It also executes branch 2 and branch 3, which are an if-branch and an invisible else-branch, respectively. These two branches are nested within branch 1. Both branches are hit by the test case because branch 1 iterates over the members of the object passed through the selected function. One member satisfies the branch 2 condition ```not name.startswith("_") and is_method```, while the rest do not.

\
**Test 2** - for function ```load_from_config(config)``` \
**New test code:** https://github.com/Kinto/kinto/commit/2fed39c78ac29409c80f9cd28e8dba0b6a4609a7 \
**Result of old coverage:**

<img width="465" alt="Mun_func2" src="https://github.com/yukikoikejiri/kinto/assets/113595508/8bf54fba-d7a0-4250-8f9e-6d7174aebbf0">

**Result of new coverage:**

<img width="465" alt="Mun_func2_new" src="https://github.com/yukikoikejiri/kinto/assets/113595508/67c97416-23fe-490c-ae3c-b74024ab4d50">

**Statement and reason of the coverage improvement:**
> The coverage from the instrumentation increased from 25% to 100%.
- Since the old test cases only tested the condition where branch 1 is executed, which contains a statement causing the function to exit, other branches were ignored. Branch 1 is executed as there is no _statsd_ module installed, a similar situation with the ```watch_execution_time``` function.
- Two new test cases have been added: ```test_load_from_config_with_project_name(self, module_mock)``` and ```test_load_from_config_without_project_name(self, module_mock)```; both of these test cases do not satisfy branch 1 condition where ```statsd_module is None```, causing the previously untested else branch (branch 2) to be executed.
- ```test_load_from_config_with_project_name(self, module_mock)``` satisfies the condition ```settings["project_name"] != ""``` for branch 3, while ```test_load_from_config_without_project_name(self, module_mock)``` does not and thus skips branch 3, proceeding to branch 4.


\
\
**Name:** Cindy-Virginia Enekwemchi \
Comparing Code: https://github.com/Kinto/kinto/compare/main...yukikoikejiri:kinto:A1_Cindy

**Test 1** - for function ```statsd_count(request, count_key)``` \
**New test code:** https://github.com/Kinto/kinto/commit/8af55f60ec02042bd8b6b2a44994cef25673f423 \
**Result of old coverage:**

<img width="467" alt="Cindy_func1" src="https://github.com/yukikoikejiri/kinto/assets/113595508/38759476-2ea6-4bd4-b3f3-b08ab80e8761">

**Result of new coverage:**

<img width="466" alt="Cindy_func1_new" src="https://github.com/yukikoikejiri/kinto/assets/113595508/4b268d9c-94b8-4150-8d40-d093cd538a68">

**Statement and reason of the coverage improvement:**
> The coverage from the function increased from 0.00% to 100.00%
- The results of the old coverage report showed that neither of the two branches in the function were covered because the existing test cases were only executed in the case the user has a _statsd_ module installed, and were thus skipped. 
- To ensure branch coverage and testing of the ```statsd_count``` function even if the user has no statsd module installed the following two new test cases have been added: ```test_statsd_count_does_not_raise_when_statsd_is_missing(self)``` and ```test_statsd_count_calls_count_method_when_statsd_is_present(self)```
- ```test_statsd_count_does_not_raise_when_statsd_is_missing(self)``` this case satisfies the else condition since the test case calls the function without _statsd_ which is none
- ```test_statsd_count_calls_count_method_when_statsd_is_present(self)``` this case does the opposite and covers the if condition, here the _statsd_ is present (mocked)  and therefore the condition satisfied
- This way both of the branches are executed and result in a coverage of a 100%

\
**Test 2** - for function ```count(self, key, count=1, unique=None)``` \
**New test code:** https://github.com/Kinto/kinto/commit/8af55f60ec02042bd8b6b2a44994cef25673f423 \
**Result of old coverage:**

<img width="466" alt="Cindy_func2" src="https://github.com/yukikoikejiri/kinto/assets/113595508/0e2530ed-2f4a-4e98-a8ae-f3f3c33cf6cc">

**Result of new coverage:**

<img width="459" alt="Cindy_func2_new" src="https://github.com/yukikoikejiri/kinto/assets/113595508/802f3df1-02e3-44f3-8fb9-ffc5080accd3">

**Statement and reason of the coverage improvement:**
> The coverage from the function increased from 0.00% to 100.00%
- The results of the old coverage report showed that neither of the two branches in the function were covered because the existing test cases were only executed in the case the user has a _statsd_ module installed, and were thus skipped. 
- To ensure branch coverage and testing of the ```count``` function even if the user has no _statsd_ module installed the following the following two new test cases have been added: ```test_count_increments_when_unique_is_none(self)``` and ```test_count_sets_value_when_unique_is_not_none(self)```
- ```test_count_increments_when_unique_is_none(self)``` this case satisfies the if condition since this test case calls the function with no unique input therefore unique is none
- ```test_count_sets_value_when_unique_is_not_none(self)``` does the opposite and therefore triggers the else condition since the input sets ```unique = "unique_value"```
- This way both of the branches are executed and result in a coverage of a 100%


\
\
**Name:** Lisa Lipkovich \
Comparing code: https://github.com/Kinto/kinto/compare/main...yukikoikejiri:kinto:A1_Lisa 

**Test 1** - for function ```create_schema(self, dry_run)``` \
**New test code:** https://github.com/Kinto/kinto/commit/26ba772b52874b9f292d98e3c567de2761feb01c \
**Result of old coverage:**

<img width="465" alt="Lisa_func1" src="https://github.com/yukikoikejiri/kinto/assets/113595508/e3f811b3-e322-480f-b553-33c9a73fd35c">

**Result of new coverage:**

<img width="461" alt="Lisa_func1_new" src="https://github.com/yukikoikejiri/kinto/assets/113595508/4a11cac4-9fdb-4953-9581-c864fd95784c">

**Statement and reason of the coverage improvement:**
> The coverage for the create_schema function increased from 0% to 100%.
- The old coverage report showed that none of the branches in the ```create_schema``` function were covered by the existing test cases. To address this, new test cases were added: ```test_create_schema_without_dry_run``` and ```test_create_schema_with_dry_run```.
- The ```test_create_schema_without_dry_run``` test case covers the ```if not dry_run``` branch (branch 1) when the ```dry_run``` parameter is ```False```. This test ensures that the _schema_ file is executed correctly, as the ```_execute_sql_file``` method is called with the specified _schema_ file.
- The ```test_create_schema_with_dry_run``` test case covers the implicit else branch (branch 2) when the ```dry_run``` parameter is ```True```. This test ensures that no changes are made to the database schema, as the ```_execute_sql_file``` method is not called.
- These two test cases ensure that all different conditional branches of the ```create_schema``` function are tested, thereby improving the overall coverage from 0% to 100%.

\
**Test 2** - for function ```__call__(self, request, *args, **kwargs)``` \
**New test code:** https://github.com/Kinto/kinto/commit/a9b884ec7c4d62e659fa26a9caa26aa2c8838515?diff=unified&w=0 \
**Result of old coverage:**

<img width="464" alt="Lisa_func2" src="https://github.com/yukikoikejiri/kinto/assets/113595508/d7d35ef7-a4d6-48dc-8717-0d894f64aa02">

**Result of new coverage:**

<img width="464" alt="Lisa_func2_new" src="https://github.com/yukikoikejiri/kinto/assets/113595508/ee817ad0-4f1c-45eb-b8b7-486a35803998">


**Statement and reason of the coverage improvement:**
> The coverage for the __call__ function increased from 77% to 100%.
- The old coverage report showed that 77% of the branches in the ```__call__``` function were covered by the existing test cases. To address the remaining gaps, new test cases were added: ```test_cache_forever_saves_result_and_updates_headers```, ```test_cache_forever_raises_value_error_for_response```, and ```test_cache_forever_uses_cached_result```.
- The ```test_cache_forever_saves_result_and_updates_headers``` test case hits the ```if self.saved is None``` branch (branch 1) and the first implicit else branch (branch 3). Since ```self.saved``` is initially ```None```, it ensures that the ```decorated``` function is called and the result is saved, covering branch 1. 
- Additionally, it verifies that when ```self.saved``` is not an instance of ```Response```, branch 3 is covered.
- The ```test_cache_forever_raises_value_error_for_response``` test case hits the ```if self.saved is None``` branch (branch 1) and the ```if isinstance(self.saved, Response)``` branch (branch 2). When the ```decorated``` function returns a ```Response```, a ```ValueError``` is raised, covering branch 2.
- The ```test_cache_forever_uses_cached_result``` test case hits the second implicit else branch (branch 4) when ```self.saved is not None```. This ensures that the cached result is used on subsequent calls, covering branch 4.
- These additional test cases ensure that all different conditional branches of the ```__call__``` function are tested, thus improving the overall coverage from 77% to 100%.


\
\
**Name:** Yukiko Ikejiri \
Comparing code: https://github.com/Kinto/kinto/compare/main...yukikoikejiri:kinto:A1_Yukiko 

**Test 1** - for function ```Storage._check_database_timezone(self)``` \
**New test code:** https://github.com/Kinto/kinto/commit/1bf4c00ce6f7418775a780f9f76c9987194c222e \
**Result of old coverage:**

<img width="465" alt="Yukiko_func1" src="https://github.com/yukikoikejiri/kinto/assets/113595508/0fc6ed25-09cc-44de-bfc1-723a551441c5">

**Result of new coverage:**

<img width="463" alt="Yukiko_func1_new" src="https://github.com/yukikoikejiri/kinto/assets/113595508/db2a587b-4b13-4930-96ec-9220b8d2be98">

**Statement and reason of the coverage improvement:**
> The coverage from the instrumentation increased from 0% to 100%. 
- The old coverage report showed that none of the branches in the function were covered by the existing test cases. New test cases have been added, namely ```test_check_database_timezone_utc(self)``` and ```test_check_database_timezone_non_utc(self)```.
- The ```test_check_database_timezone_utc``` test case hits the else branch (branch 2) when the database timezone is UTC. Since the mocked database response returns the UTC timezone, calling the ```self.storage._check_database_timezone()``` method executes the else branch, and no exception is raised.
- The ```test_check_database_timezone_non_utc``` test case hits the if branch (branch 1) when the database timezone is not UTC. Since the mocked database response returns the PST timezone, calling the ```self.storage._check_database_timezone()``` method executes the if branch, and a warning is raised.
- These two test cases ensure that all different conditional branches of the function are tested, thus improving overall coverage.

\
**Test 2** - for function ```Storage._check_database_encoding(self)``` \
**New test code:** https://github.com/Kinto/kinto/commit/3ff5c8348f15af512816b0355d3d6a51977387a7 \
**Result of old coverage:**

<img width="466" alt="Yukiko_func2" src="https://github.com/yukikoikejiri/kinto/assets/113595508/8df1080d-8253-4117-960a-6a7c16c00540">

**Result of new coverage:**

<img width="467" alt="Yukiko_func2_new" src="https://github.com/yukikoikejiri/kinto/assets/113595508/c2215eaa-5ea3-4ac6-b082-ce2439569c42">

**Statement and reason of the coverage improvement:**
> The coverage from the instrumentation increased from 0% to 100%. 
- The old coverage report showed that none of the branches in the function were covered by the existing test cases. New test cases have been added, namely ```test_check_database_encoding_utf8(self)``` and ```test_check_database_encoding_non_utf8(self)```.
- The ```test_check_database_encoding_utf8``` test case hits the else branch (branch 2) when the database encoding is UTF-8. Since the mocked database response returns the UTF-8 encoding, calling the ```self.storage._check_database_encoding()``` function executes the else branch, and no exception is raised.
- The ```test_check_database_encoding_non_utf8``` test case hits the if branch (branch 1) when the database encoding is not UTF-8. Since the mocked database response returns the Latin-1 encoding, calling the ```self.storage._check_database_encoding()``` function executes the if branch, and an ```AssertionError``` is raised.
- These two test cases ensure that all different conditional branches of the function are tested, thus improving overall coverage.

### Overall

**Results of the old coverage by running the existing tool:**
- Coverage report: 87%
> Link to the [screenshot](https://drive.google.com/file/d/1zhVf29ru1ji9dSbwJ45Req72xLHChiUe/view?usp=drive_link) \
> Link to the [html files](https://drive.google.com/file/d/1_RrgHzZo1sa60eLcNcWoIA7hAc_Az6AF/view?usp=sharing)

**Results of the new coverage by running the existing tool:**
- Coverage report: 87%
> Link to the [screenshot](https://drive.google.com/file/d/1Dj3mlE_gt99wX0ZwirFEV8smRulmhs9X/view?usp=sharing) \
> Link to the [html files](https://drive.google.com/file/d/1Lxva5iKS2AbuC_7MTZv4xX1lyIwoRvDk/view?usp=sharing)

New coverage results for each function by running the existing tool:

<img width="477" alt="image" src="https://github.com/yukikoikejiri/kinto/assets/113595508/f27d0ef1-72d4-4d84-a297-6a83f1968e93">


## Statement of individual contributions

**Name:** Charanan Mahakijpalach \
**Responsibilities:** 
- Provided a guideline structure for the README
- Ran the existing tool to see the result along with the other team members
- Created own instrumentation tool with report for functions `watch_execution_time` and `load_from_config`
- Provided additional test cases for the previously mentioned functions to improve branch coverage
- Reviewed and merged a pull request

**Name:** Cindy-Virginia Enekwemchi \
**Responsibilities:** 
- Ran coverage tool to compare and verify sameness of the report results
- Created own instrumentation tool with report for functions `count` and `statsd_count`
- Provided additional test cases for the previously mentioned functions to improve branch coverage
- Reported on my instrumentation and coverage in this file
- Reviewed a pull request and merged it

**Name:** Lisa Lipkovich \
**Responsibilities:**
- Created own instrumentation tool for functions `create_schema` and `__call__`
- Provided additional test cases for the previously mentioned functions to improve branch coverage
- Reported on my instrumentation and coverage in this file

**Name:** Yukiko Ikejiri \
**Responsibilities:**
- Found the project for the team
- Counted LOC by Lizard
- Being a baseline coverage using existing tool for both old and new results
- Created own instrumentation tool with report for functions `Storage._check_database_timezone` and `Storage._check_database_encoding`
- Provided additional test cases for the previously mentioned functions to improve branch coverage
- Reviewed and merged pull requests

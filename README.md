# py_project


| Test<br>Case<br>ID | Test Case | Test Steps | Test Data | Expected Results| Actual Results | Pass/Fail |
|------ | --- | --- | --- | --- | --- | --- |
| TU01 |  Check if each checkbox field is selectable | 1. Go to https://onex.am/en  <br> 2. Choose CALCULATOR OF SHIPPING in the right corner <br> 3. Select one or more options in specified field | | The specific option should be selected | As expected | Pass |   
| TU02 | Check if each checkbox field's selection enables the specific element as selected by mouse pointer or keyboard selection | 1. Go to https://onex.am/en  <br> 2. Choose CALCULATOR OF SHIPPING in the right corner <br> 3. Select one or more options with mouse pointer in specified field <br> 4. Use keyboard's Right and Left arrow keys for selecting options after selecting any option with mouse pointer in that field | | The specific element should be selected both with keyboard keys and mouse pointer | As expected | Pass | 
| TU03 | Check if the multiple options can be selected in each checkbox field | 1. Go to https://onex.am/en  <br> 2. Choose CALCULATOR OF SHIPPING in the right corner <br> 3. Select two or more options | | Two or more options shouldn't be selected | As expected | Pass
| TU04 | Verify if the initial focus of the checkbox fields is on the first checkbox.| 1. Go to https://onex.am/en  <br> 2. Choose CALCULATOR OF SHIPPING in the right corner <br> 3. Make sure if the first checkbox is selected | | Initially the first checkbox should be selected | As expected | Pass
| TI05 | Check if the selection marks work independetly for each checkbox field| 1. Go to https://onex.am/en  <br> 2. Choose CALCULATOR OF SHIPPING in the right corner <br> 3. Make sure if the selection mark works independently for WAREHOUSE COUNTRY field <br> 4. Make sure if the selection mark works independently for TYPE OF ORDER field <br> 5. Make sure if the selection mark works independently for SHIPPING METHOD field  | | Selection marks should be worked independently | Independency works partly, for first two US flags independency works when I go from left to right, but when I go from right to left it doesn't work, independency doesn't work for rest flags | Fail
| TU06 | Check SHIPPING COST giving valid input data |  1. Go to https://onex.am/en <br> 2.Choose CALCULATOR OF SHIPPING in the right corner 3. Write positive number in Real Weight input 4. Check SHIPPING COST field | COUNTRY: US <br> TYPE OF ORDER: ONLINE SHOPPING <br> SHIPPING METHOD: BY AIR <br> Real Weight/kg: 0 | 0 AMD | 400 AMD | Fail
|||||| COUNTRY: US <br> TYPE OF ORDER: ONLINE SHOPPING <br> SHIPPING METHOD: BY AIR <br> Real Weight/kg: 0.1 | 400 AMD | 400 AMD | Pass
Only in c) all values are from the same class(3). So the answer is c) 22,23,24  













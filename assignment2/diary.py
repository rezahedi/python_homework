import traceback
from datetime import date

isFirst = True

try:
  today = date.today()
  with open('diary.txt', 'w') as file:
    file.write(f'Diary of {today.strftime('%a %d %b %Y')}\n\n')
    # Infinite loop!
    while True:
      response = input('What happened today? (Type end to exit) ' if isFirst else 'What else? (Type end to exit) ')
      isFirst = False

      file.write(f'{response}\n')

      if response == 'end':
        break

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")

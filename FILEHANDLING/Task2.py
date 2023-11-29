
import datetime
import time
def Custome_decoretor(path="log.txt"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time

                # Log to file
                with open(path, "a") as log:
                    log.write(
                        f"{datetime.datetime.now()} - "
                        f"Function '{func.__name__}' executed in {execution_time:.6f} seconds.\n"
                    )

                return result

            except Exception as e:
                # Log exception to file
                with open(path, "a") as log:
                    log.write(
                        f"{datetime.datetime.now()} - "
                        f"Exception in function '{func.__name__}': {str(e)}\n"
                    )

                # Re-raise the exception
                raise e

        return wrapper
    return decorator

@Custome_decoretor()
def example_function(num):
    print("Executing example_function...")
    for i in range(num):
        print(i)
example_function(20)
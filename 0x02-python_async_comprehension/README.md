#  0x02. Python - Async Comprehension  

For this project, I began practicing using the Python for my specialization into backend development, more specifically i delved into the world of Async Programming.

![alt text](image.png)

**Tags: [Python, Back-end]**

## Tasks :page_with_curl:



0. **Async Generator mandatory**
  * [0-async_generator](./0-async_generator.py): Write a coroutine called async_generator that takes no arguments.

    The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module. 

  **Use the random module.**



* **1. Async Comprehensions**
    * [1-async_comprehension](./1-async_comprehension.py): Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.

    The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.




* **2. Run time for four parallel comprehensions**
  * [2-measure_runtime](./2-measure_runtime.py): Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.

    measure_runtime should measure the total runtime and return it.

    **Notice that the total runtime is roughly 10 seconds, explain it to yourself.**
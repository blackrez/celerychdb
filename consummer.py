from task import query



task = query.apply_async()
task_id = task.task_id
query_results = query.AsyncResult(task_id)
while query_results.status == "PENDING":
	print(query_results.status)
	query_results = query.AsyncResult(task_id)
# At the end
if query_results.status == "SUCCESS":
	print(query_results.result)
else:
	print("FAILED")
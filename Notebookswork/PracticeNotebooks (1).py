# Databricks notebook source
# MAGIC %run ../../Includes/Classroom-Setup-01.2

# COMMAND ----------

print(f"DA:                   {DA}")
print(f"DA.Username:           {DA.username}")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT '${da.username}' AS current_username,
# MAGIC        '${da.paths.working_dir}' AS working_directories

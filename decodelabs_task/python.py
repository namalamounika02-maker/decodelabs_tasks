{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9594aa90-cf40-451d-a39e-8f8a7d646a15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a task (or type 'done' to finish):  finish \n",
      "Enter a task (or type 'done' to finish):  tiffin\n",
      "Enter a task (or type 'done' to finish):  done\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Your To-Do List:\n",
      "- finish \n",
      "- tiffin\n"
     ]
    }
   ],
   "source": [
    "tasks = []\n",
    "\n",
    "while True:\n",
    "    task = input(\"Enter a task (or type 'done' to finish): \")\n",
    "\n",
    "    if task.lower() == \"done\":\n",
    "        break\n",
    "\n",
    "    tasks.append(task)\n",
    "\n",
    "print(\"\\nYour To-Do List:\")\n",
    "\n",
    "for task in tasks:\n",
    "    print(\"-\", task)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18106314-a9d3-49a6-90fb-f4982b7f9df0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

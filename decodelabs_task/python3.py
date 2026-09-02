{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "44acaf8d-6804-4dab-800d-85097210ae40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter password length (e.g., 8):  7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generated password: kveZUNk\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import random\n",
    "\n",
    "# Characters that can be used in the password\n",
    "letters = \"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\"\n",
    "numbers = \"0123456789\"\n",
    "\n",
    "# Combine letters and numbers\n",
    "characters = letters + numbers\n",
    "\n",
    "# Ask the user for the password length\n",
    "length = int(input(\"Enter password length (e.g., 8): \"))\n",
    "\n",
    "# Generate the password\n",
    "password = \"\"\n",
    "\n",
    "for i in range(length):\n",
    "    password += random.choice(characters)\n",
    "\n",
    "# Display the generated password\n",
    "print(\"Generated password:\", password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b0c7531-bd29-41aa-9a07-acb91e1520f2",
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

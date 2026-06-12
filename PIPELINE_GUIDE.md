# Cash Withdrawal System - Pipeline Guide

## Goal: Implement Verification & Withdrawal/Deposit Features

---

## PART 1: VERIFICATION FEATURE ✓

Your `verify_user()` function needs to:

### Step 1.1: Check if User ID Exists
- **Logic**: Loop through the `users` dictionary
- **Hint**: Use `for user_key in users:` or `for user_obj in users.values()`
- **Question to ask yourself**: How do I compare the input ID with each user's ID?
- **Goal**: Find if any user has matching `user_id`

### Step 1.2: If ID Found, Check PIN
- **Logic**: Once you find a matching user ID, verify their PIN
- **Hint**: Access the user object: `users[user_key].account_pin`
- **Question to ask yourself**: Should I compare with `==`?
- **Goal**: Confirm the PIN matches

### Step 1.3: Return Verification Result
- **Option A**: Return `True` if verified, `False` if not
- **Option B**: Return the user object if verified, `None` if not
- **Hint**: Option B is more useful because you'll need the user object for deposits/withdrawals
- **Goal**: Can your other functions use this result?

### Step 1.4: Error Handling
- What if the ID doesn't exist?
- What if the PIN is wrong?
- Should you give hints to attackers? (Security question - think about this!)
- **Hint**: Consider using `print()` for feedback messages

---

## PART 2: WITHDRAWAL FEATURE ✓

### Step 2.1: Get Withdrawal Amount
- **Logic**: Ask user how much they want to withdraw
- **Hint**: Use `input()` and convert to `float()`
- **Question to ask yourself**: What if they enter negative numbers or text?

### Step 2.2: Validate the Withdrawal
- Check 1: Is the amount positive?
- Check 2: Is the amount <= their current balance?
- Check 3: Is the amount a valid number?
- **Hint**: Use `if` and `elif` statements
- **Goal**: Prevent invalid transactions

### Step 2.3: Update the Balance
- **Logic**: Subtract the withdrawal from user's balance
- **Hint**: `user.balance = user.balance - amount` OR `user.balance -= amount`
- **Question to ask yourself**: Where is the balance stored?

### Step 2.4: Confirm the Transaction
- Print the new balance
- Print a success message
- **Hint**: Use f-strings: `f"New balance: ${user.balance}"`

### Step 2.5: Return/Store Result
- **Question**: Should this function return anything?
- **Hint**: Think about what the main program needs to know

---

## PART 3: DEPOSIT FEATURE ✓

### Step 3.1: Get Deposit Amount
- **Logic**: Ask user how much they want to deposit
- **Hint**: Very similar to withdrawal step 2.1
- **Question to ask yourself**: Can this be reused or should it be separate?

### Step 3.2: Validate the Deposit
- Check 1: Is the amount positive?
- Check 2: Is the amount a valid number?
- **Hint**: Deposits don't need balance check (can't deposit more than you have)
- **Different from withdrawal**: Fewer validation checks needed

### Step 3.3: Update the Balance
- **Logic**: Add the deposit to user's balance
- **Hint**: `user.balance = user.balance + amount` OR `user.balance += amount`
- **Question to ask yourself**: Same storage location as withdrawal?

### Step 3.4: Confirm the Transaction
- Print the new balance
- Print a success message

---

## MAIN FLOW (How to Connect Everything)

```
1. Create account (already done ✓)
2. Verify user
   ├─ Valid? → Go to menu
   └─ Invalid? → Try again or exit
3. Show menu to user:
   ├─ Withdraw
   ├─ Deposit
   ├─ Check balance
   └─ Exit
4. Process their choice
   ├─ Call withdrawal function
   ├─ Call deposit function
   ├─ Display balance
   └─ Ask for next action
5. Loop until user exits
```

---

## LEARNING TIPS

### For Verification:
- **Start small**: First, just make it check if ID exists
- **Then add**: PIN verification
- **Then refine**: Better error messages
- **Test**: Create 2-3 test users first, then manually test verify_user()

### For Withdrawal/Deposit:
- **Start with withdrawal**: It has more validation rules
- **Copy the pattern to deposit**: Then simplify (fewer checks)
- **Test edge cases**: What if someone withdraws exactly their balance?
- **Test invalid inputs**: What if they enter -100 or "abc"?

### Debugging Tips:
- Use `print()` statements to see what's happening
- Example: `print(f"Looking for ID: {verify_id}")` inside your loop
- Example: `print(f"User found: {user_key}")` when you find a match

---

## Syntax Reminders

### Dictionary Access:
```python
# Loop through users and check their properties
for key in users:
    user = users[key]
    if user.user_id == something:
        # found it!

# Or shorter:
for user in users.values():
    if user.user_id == something:
        # found it!
```

### Modifying Object Properties:
```python
user.balance = user.balance - amount  # Withdrawal
user.balance += amount                 # Deposit (shorter syntax)
```

### Conditional Logic:
```python
if amount <= 0:
    print("Amount must be positive!")
elif amount > user.balance:
    print("Insufficient funds!")
else:
    # Process withdrawal
```

---

## Your Challenges for Tonight

1. **Complete `verify_user()`** - Should return the verified user object
2. **Create `withdraw_funds(user)`** - Takes user object, handles withdrawal
3. **Create `deposit_funds(user)`** - Takes user object, handles deposit
4. **Add a main menu** - After verification, ask what user wants to do
5. **Add a loop** - Let user do multiple transactions

Start with verification, then do withdrawal (more complex), then deposit!

Good luck! 🚀

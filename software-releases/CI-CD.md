# CI and CD

> _Software Development Life Cycle_

### CI CD is about automation of the automation of `software development lifecycle`.

> **CODE -> BUILD -> TEST -> DEPLOY -> PROVISION**

## CI CD involves 2 Stages :

### Continuous Integration ( CI )

- Code Builds and testings

# **D** might be `Delivery or Deployment`

### Continuous Delivery ( CD )

- Involves manual approvals

### Continuous Deployment ( CD )

- Involves no manual approvals **( Complete Automation )**

---

## _2 steps are needed to be addressed :_

- Protect the `master branch` at **`github website`**
- Enable `build` on forks option must be enabled on **`circleci website`**

---

### !! Remember `Github` can ony host but not **`execute` code bundle** .

That's why we use `3rd party ci servers`to execute the code ie., **circleci , travisci , jenkins , etc ..**

---

> ## CI CD helps in TDD Project's

- **Builds**
- **Tests**
- **Lints**
- **Code Quality and Standard styles**
- **Generating Test Coverage Reports**

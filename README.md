# Python Playwright BDD Test Suite

An automated end-to-end test suite for the [Sauce Demo](https://www.saucedemo.com) e-commerce application, built with Python, Playwright, and Behave (BDD).

## Tech Stack

| Tool | Purpose |
|------|---------|
| [Python](https://www.python.org/) | Programming language |
| [Playwright](https://playwright.dev/python/) | Browser automation |
| [Behave](https://behave.readthedocs.io/) | BDD test framework (Gherkin) |
| Chromium | Default browser (headed mode) |

## Project Structure

```
PythonPlaywright/
├── features/
│   ├── environment.py          # Behave hooks (browser setup/teardown, logging)
│   ├── steps/
│   │   ├── locators.py         # Centralised CSS selectors
│   │   ├── login.py            # Login step definitions
│   │   ├── userlogin.py        # User login step definitions
│   │   ├── Addproducttocart.py
│   │   ├── Cartnavigation.py
│   │   ├── Removeproductfromcart.py
│   │   └── ...                 # Other step definition files
│   ├── login.feature
│   ├── Userslogin.feature
│   ├── Addproducttocart.feature
│   ├── OrderJourneyofproduct.feature
│   └── ...                     # Other feature files
├── venv/                       # Python virtual environment
├── playwright.bat              # Windows helper to activate venv
└── README.md
```

## Test Coverage

### Authentication
- `login.feature` — Standard, performance glitch, problem, visual, and error user logins
- `Userslogin.feature` — Locked user, incorrect credentials, empty fields, case sensitivity
- `LoginProblemUser.feature` — Problem user-specific behaviour

### Product & Navigation
- `Productnavigation.feature` — Navigate to product detail pages
- `Verifyproductdetailsafternavigating.feature` — Product details verification
- `Sortbyfilters.feature` — Sort by name and price filters
- `Downloadimage.feature` — Product image download

### Cart
- `Addproducttocart.feature` — Add single and multiple products
- `Displaycart.feature` — Cart contents display
- `Cartnavigation.feature` — Cart navigation flow
- `Cartemptycheckout.feature` — Checkout with empty cart
- `Removeallproductsfromcart.feature` — Remove all items
- `Removesingleproductfromcart.feature` — Remove a specific item

### Checkout & Orders
- `OrderJourneyofproduct.feature` — Full purchase journey
- `Multipleordersjourney.feature` — Ordering multiple products
- `CustomerOverviewpageatcheckoutflow.feature` — Order summary page
- `Customerconfirmationatcheckoutflow.feature` — Order confirmation page
- `CancelOrderatCheckoutState.feature` — Cancel at checkout
- `CheckoutFormValidation.feature` — Form field validation
- `OrderConfirmationpage.feature` — Post-order confirmation
- `Unabletoplaceorderfromerroruser.feature` — Error user checkout restrictions

### UI & Miscellaneous
- `HamburgerMenu.feature` — Side menu navigation
- `FooterNavigation.feature` — Footer links (Twitter, Facebook, LinkedIn)
- `ContinueShopping.feature` — Continue shopping from cart
- `VisualUser.feature` — Visual user-specific UI checks

## Prerequisites

- Python 3.8+
- pip

## Setup

```bash
# 1. Clone the repository
git clone <repo-url>
cd PythonPlaywright

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install behave playwright

# 4. Install Playwright browsers
playwright install chromium
```

## Running Tests

```bash
# Run all feature files
behave

# Run a specific feature file
behave features/login.feature

# Run scenarios with a specific tag
behave --tags=@tested

# Run in headless mode (set headless=True in environment.py)
behave
```

## Logging & Screenshots

Each feature run automatically generates:
- A `.log` file alongside the feature file (overwritten on each run)
- A `.png` screenshot path configured per feature (taken in step definitions as needed)

## Test Users

All test users use the password `secret_sauce`.

| Username | Behaviour |
|----------|-----------|
| `standard_user` | Normal e-commerce flow |
| `locked_out_user` | Login blocked |
| `problem_user` | UI defects on product pages |
| `performance_glitch_user` | Slow page loads |
| `error_user` | Errors during checkout |
| `visual_user` | Visual layout differences |

## Windows Quick Start

Double-click `playwright.bat` to open a terminal with the virtual environment already activated.

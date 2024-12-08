<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">DATASET-GENERATION-FAKER.GIT</h1></p>
<p align="center">
	<em>Crafting Tomorrow's Data, Today's Rules</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/yann-furrer/Dataset-generation-faker.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/yann-furrer/Dataset-generation-faker.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/yann-furrer/Dataset-generation-faker.git?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/yann-furrer/Dataset-generation-faker.git?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The Dataset-generation-faker.git project revolutionizes the creation of synthetic data for testing and simulation. By leveraging a rule-based engine, it generates realistic datasets that adhere to or intentionally violate predefined configurations. Ideal for developers and QA engineers, this tool enhances testing accuracy and efficiency, ensuring robust software solutions across various use cases.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a rule engine architecture as outlined in `architecture.txt`.</li><li>Includes a mix of Python scripts and configuration files (`YAML`, `JSON`) for dynamic dataset generation.</li><li>Structured into core functionalities for rule execution and dataset generation, and utilities for data manipulation.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Codebase includes modular Python scripts for different functionalities like dataset generation and rule processing.</li><li>Utilizes class extensions for dynamic method enhancements in `core/class_extensions.py`.</li><li>Follows a clear separation of concerns between data generation, configuration management, and utility functions.</li></ul> |
| 📄 | **Documentation** | <ul><li>Documentation includes usage of `pip` for dependency management as specified in `requirements.txt`.</li><li>Code comments and structured documentation available in primary language Python.</li><li>Installation and usage commands are clearly documented for setup and operational guidance.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Supports extensive use of external libraries and frameworks managed via `pip`.</li><li>Integrates with JSON and YAML for configuration and rule definitions.</li><li>Designed to facilitate easy integration with other Python-based tools and libraries.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Highly modular design with separate components for core functionalities (`core/engine.py`), data generation (`core/dataset_factory.py`), and utilities (`utils/extract.py`).</li><li>Enables easy extension and customization of dataset and rule configurations.</li><li>Modular architecture supports independent testing and maintenance.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes test commands using `pytest` as documented.</li><li>Supports testing of individual modules as well as integrated rule and dataset generation functionalities.</li><li>Facilitates robust testing scenarios by generating datasets that intentionally violate specified rules (`generator/rules_generator.py`).</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized for performance with batch data storage and minimal memory usage during dataset generation.</li><li>Efficient data manipulation and extraction techniques in utility scripts.</li><li>Performance considerations in handling large and complex data structures.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Focuses on secure handling of data files and configurations.</li><li>Implements data validation and rule checks to prevent incorrect data manipulations.</li><li>No specific security tools or protocols detailed, suggesting an area for potential enhancement.</li></ul> |

---

## 📁 Project Structure

```sh
└── Dataset-generation-faker.git/
    ├── Architecture.txt
    ├── config
    │   ├── dataset_config.yaml
    │   ├── dataset_example.yaml
    │   └── rules_config.json
    ├── core
    │   ├── class_extensions.py
    │   ├── dataset_factory.py
    │   ├── engine.py
    │   └── utils_core.py
    ├── generator
    │   ├── rules_generator.py
    │   └── yaml_generator.py
    ├── main.py
    ├── requirements.txt
    └── utils
        ├── extract.py
        └── load.py
```


### 📂 Project Index
<details open>
	<summary><b><code>DATASET-GENERATION-FAKER.GIT/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/main.py'>main.py</a></b></td>
				<td>- Main.py orchestrates the generation of dataset records by loading configurations, extracting necessary paths and field types, and executing defined rules<br>- It handles both standard and random rule executions to ensure the desired number of records is generated, adapting to rule failures by inverting and reapplying rules as needed.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Manages and lists the dependencies necessary for the project, ensuring that all required Python packages are installed to maintain the functionality and stability of the software<br>- Located within the project's structure, it plays a crucial role in setting up environments, particularly for new installations or updates.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/Architecture.txt'>Architecture.txt</a></b></td>
				<td>- Architecture.txt outlines the structure of a rule engine project, detailing directories for configurations, generators, core functionalities, and utilities<br>- It includes YAML and JSON configuration files, Python scripts for generating these files, a core engine for rule execution, dataset generation, and utility scripts for validation and logging, ensuring a comprehensive setup for rule-based operations.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- core Submodule -->
		<summary><b>core</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/core/dataset_factory.py'>dataset_factory.py</a></b></td>
				<td>- Generates synthetic datasets based on predefined configurations and rules specified in a YAML file<br>- It supports various data types including strings, integers, dates, booleans, arrays, and objects, allowing for the creation of complex nested data structures<br>- This functionality is crucial for testing and simulation purposes within the project.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/core/class_extensions.py'>class_extensions.py</a></b></td>
				<td>- Enhances class functionality by dynamically adding methods that retrieve nested data from objects based on specified paths<br>- It utilizes regular expressions to parse paths and applies appropriate decorators to the methods based on their return types, ensuring they conform to business rules.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/core/engine.py'>engine.py</a></b></td>
				<td>- Core/engine.py serves as the central processing unit for dynamic data generation and rule-based validation within the system<br>- It facilitates the creation of JSON data structures based on predefined business rules, manages the execution of these rules, and handles the batch storage of results to optimize memory usage.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/core/utils_core.py'>utils_core.py</a></b></td>
				<td>- Enhances the project's ability to dynamically manipulate and analyze data structures by providing utilities for extracting types, field names, and paths from nested configurations, and updating values within these structures based on specified paths<br>- These tools support flexible data handling and configuration management across the application.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- generator Submodule -->
		<summary><b>generator</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/generator/yaml_generator.py'>yaml_generator.py</a></b></td>
				<td>- Generates and structures YAML data by flattening nested objects and determining their types, which facilitates the creation of a hierarchical schema<br>- This process is crucial for managing complex data structures within the project, allowing for clearer data manipulation and schema generation.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/generator/rules_generator.py'>rules_generator.py</a></b></td>
				<td>- Generator/rules_generator.py serves as a tool within the project to create a set of inverted conditions from the rules defined in rules_amf.json<br>- It modifies rule operators to generate data that intentionally violates the specified rules, aiding in testing and validation processes by ensuring robustness against rule breaches.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- config Submodule -->
		<summary><b>config</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/config/rules_config.json'>rules_config.json</a></b></td>
				<td>- Configures rules within the system, specifying conditions under which certain actions are triggered<br>- In the provided example, it defines a rule where an action is executed if a specific boolean condition is met, with a limit on the number of occurrences<br>- This setup is crucial for managing automated responses based on predefined criteria across the application.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/config/dataset_example.yaml'>dataset_example.yaml</a></b></td>
				<td>- Defines a configuration for generating a dataset named UserProfiles, specifying the structure and characteristics of various fields such as fullName, email, age, and nested objects<br>- It includes data types, constraints like age and revenue ranges, and uses faker types for realistic data simulation, supporting complex nested structures and arrays.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/config/dataset_config.yaml'>dataset_config.yaml</a></b></td>
				<td>- Defines the configuration for a dataset named 'messageAMF', specifying the structure and rules for generating synthetic data records<br>- It includes various fields such as boolean, date, and complex objects with nested fields, tailored for email message simulations, ensuring data variety and realism in testing environments.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- utils Submodule -->
		<summary><b>utils</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/utils/extract.py'>extract.py</a></b></td>
				<td>- Manages data file operations within the dataset directory, including creating new files, appending batches of data to existing JSON files, and generating CSV files from dictionary data<br>- Ensures efficient data handling without loading entire files into memory, preventing data duplication and errors in file management.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/yann-furrer/Dataset-generation-faker.git/blob/master/utils/load.py'>load.py</a></b></td>
				<td>- Load.py serves as a configuration loader within the codebase, facilitating the retrieval of rule sets and dataset configurations essential for the application's operation<br>- It dynamically fetches rules from JSON files based on specified criteria and extracts dataset parameters from a YAML file, ensuring the application adapts to various operational scenarios efficiently.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Dataset-generation-faker.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


### ⚙️ Installation

Install Dataset-generation-faker.git using one of the following methods:

**Build from source:**

1. Clone the Dataset-generation-faker.git repository:
```sh
❯ git clone https://github.com/yann-furrer/Dataset-generation-faker.git
```

2. Navigate to the project directory:
```sh
❯ cd Dataset-generation-faker.git
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




### 🤖 Usage
Run Dataset-generation-faker.git using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/yann-furrer/Dataset-generation-faker.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/yann-furrer/Dataset-generation-faker.git/issues)**: Submit bugs found or log feature requests for the `Dataset-generation-faker.git` project.
- **💡 [Submit Pull Requests](https://github.com/yann-furrer/Dataset-generation-faker.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/yann-furrer/Dataset-generation-faker.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/yann-furrer/Dataset-generation-faker.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=yann-furrer/Dataset-generation-faker.git">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
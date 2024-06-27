# Indigenous Friendship Centres Info

This is a simple command-line tool to fetch and display information about Indigenous Friendship Centres in Ontario, Canada. It provides contact details and the services offered by each centre.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/indigenous-friendship-centres.git
   ```

2. Navigate to the project directory:
   ```sh
   cd indigenous-friendship-centres
   ```

3. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

4. Install required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Display Information for All Centres

To get information about all centres:
```sh
python friendship_centres.py --all
```

### Display Information for a Specific Centre

To get information about a specific centre by name:
```sh
python friendship_centres.py --name "Hamilton Regional Indian Centre"
```

## Example Output

### All Centres

```sh
$ python friendship_centres.py --all

Name: Brantford Regional Indigenous Support Centre (BRISC)
Address: 318 1/2 Colborne Street E., Brantford, ON N3S 3N1
Phone: 519-304-7400
Services:
  - Healing and Wellness Coordinator Program
  - Indigenous Court Work Program
  - Education and Employment
  - Homelessness and Housing
  - Apatisiwin - Employment & Training Program
  - Urban programming for Indigenous people

...

```

### Specific Centre

```sh
$ python friendship_centres.py --name "Hamilton Regional Indian Centre"

Name: Hamilton Regional Indian Centre
Address: 34 Ottawa St. North, Hamilton, ON L8H 3Y7
Phone: 905-545-4077
Email: support@hric.ca
Website: http://www.hric.ca
Services:
  - Strengthening Hamilton Aboriginal Education (SHAE)
  - Apatisiwin - Employment & Training Program
  - Aboriginal Alcohol/Drug Program
  - Aboriginal Criminal/Family Court Work Program
  - Aboriginal Family Support Program
  - Aboriginal Healthy Babies/Healthy Children Program
  - Aboriginal Prenatal/Nutrition Program
  - Fetal Alcohol Spectrum Disorder (FASD) and Nutrition Program
  - Indigenous Youth Wellness Program

...

```

## Contributing

We welcome contributions to enhance this tool. You can contribute by:

- Reporting bugs
- Suggesting features
- Submitting pull requests

### Steps to Contribute

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please open an issue in the repository or contact us at info@example.com.
```

### Repository Structure

Ensure your repository has the following structure:

```
indigenous-friendship-centres/
│
├── LICENSE
├── README.md
├── requirements.txt
└── friendship_centres.py
```

### Steps to Publish and Share

1. **Initialize a Local Repository:**
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create a Remote Repository on GitHub:**
   - Go to [GitHub](https://github.com) and create a new repository named `indigenous-friendship-centres`.

3. **Link the Local Repository to GitHub:**
   ```sh
   git remote add origin https://github.com/yourusername/indigenous-friendship-centres.git
   git push -u origin master
   ```

4. **Share the Repository:**
   - Share the URL of your GitHub repository (e.g., `https://github.com/yourusername/indigenous-friendship-centres`) so others can access, use, and contribute to your tool.

By following these steps, your script will be publicly available and others can use and contribute to it.

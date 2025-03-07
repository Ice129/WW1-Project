//This file is used alongside Test_Database_Table to test javascript to call info from database
//Wait for DOM to be fully loaded before executing further code
document.addEventListener("DOMContentLoaded", () => {
  //Define search parameters for database query
    const postData = {
      databaseName: "rollofhonour",
      forename: "",
      surname: "",
      regiment: ""
    };
  //Make API request to fetch the data from SQL server
    fetch("http://localhost:8000/get_data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(postData)
    })
    //Parse, then process data returned from server
    .then(response => response.json())
    .then(data => {
      const tbody = document.querySelector('#testTable tbody');
      tbody.innerHTML = '';
      //Incase no data is returned
      if (data.length === 0) {
        tbody.innerHTML = '<tr><td colspan="22">No records found.</td></tr>';
        return;
      }
      //Iterate through each data item and creates table rows
      data.forEach(item => {
        const row = `<tr>
          <td>${item.surname}</td>
          <td>${item.forename}</td>
          <td>${item.address}</td>
          <td>${item.electoral_ward}</td>
          <td>${item.town}</td>
          <td>${item.rank}</td>
          <td>${item.regiment}</td>
          <td>${item.unit}</td>
          <td>${item.company}</td>
          <td>${item.age}</td>
          <td>${item.service_no}</td>
          <td>${item.other_regiment}</td>
          <td>${item.other_service_no}</td>
          <td>${item.medals}</td>
          <td>${item.enlisted_date}</td>
          <td>${item.discharged_date}</td>
          <td>${item.death_date}</td>
          <td>${item.misc_info_nroh}</td>
          <td>${item.cemetery_memorial}</td>
          <td>${item.cemetery_memorial_ref}</td>
          <td>${item.cemetery_memorial_country}</td>
          <td>${item.additional_cwgc_info}</td>
        </tr>`;
        //Adds the new row to the table
        tbody.insertAdjacentHTML('beforeend', row);
      });
    })
    //Handles errors the may occur during the fetch operation
    .catch(error => {
      console.error("Error fetching data:", error);
      const tbody = document.querySelector('#testTable tbody');
      tbody.innerHTML = '<tr><td colspan="22">Error loading data.</td></tr>';
    });
  });
  
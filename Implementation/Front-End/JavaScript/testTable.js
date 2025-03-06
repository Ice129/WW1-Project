document.addEventListener("DOMContentLoaded", () => {
    const postData = {
      databaseName: "rollofhonour",
      surname: "",
      forename: "",
      regiment: ""
    };
  
    fetch("http://localhost:8000/get_data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(postData)
    })
    .then(response => response.json())
    .then(data => {
      const tbody = document.querySelector('#testTable tbody');
      tbody.innerHTML = ''; // Clear the loading row
  
      if (data.length === 0) {
        tbody.innerHTML = '<tr><td colspan="4">No records found.</td></tr>';
        return;
      }
  
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
        tbody.insertAdjacentHTML('beforeend', row);
      });
    })
    .catch(error => {
      console.error("Error fetching data:", error);
      const tbody = document.querySelector('#testTable tbody');
      tbody.innerHTML = '<tr><td colspan="4">Error loading data.</td></tr>';
    });
  });
  
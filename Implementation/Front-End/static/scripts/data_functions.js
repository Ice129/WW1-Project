export function fetchData(forename, surname, regiment, databaseName) {
    const url = '/get_data';
    const body = {
        databaseName: databaseName,
        forename: forename,
        surname: surname,
        regiment: regiment
    };

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Ensure the content type is JSON
        },
        body: JSON.stringify(body)  // Convert the body to a JSON string
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => {
                console.error('Validation Error:', err);
                throw new Error('Validation Error');
            });
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data);
        return data;
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}
// from data.js
let tableData = data;

// console log the data 
console.log('tableData:', tableData);

// Get a reference to the table body
let tbody = d3.select('tbody');

// Create a function that will generate the table 
function createTable(ufoData){
// Use d3 to update each cell's text with ufo sighting info
    data.forEach((tableData)=> {
        let row = tbody.append('tr');
        Object.entries(tableData).forEach(([key,value]) => {
            let cell = row.append('td');
            cell.text(value);
        });
    });
};

// Call the createTable function to create the table on the page 
createTable(tableData);

// Get a reference to the filter button
let filterButton = d3.select('#filter-btn');

// Use d3 to filter the on the date and save in filterData letiable 
filterButton.on('click', function() {
    d3.event.preventDefault();
    tbody.selectAll('*').remove();
    let dateFilter = d3.select("#datetime").property('value');
    let filterData = tableData.filter(x => x.datetime === dateFilter);

   // Use d3 to update each cell's text with filtered data
    filterData.forEach((tableData)=> {
        let row = tbody.append('tr');
        Object.entries(tableData).forEach(([key,value]) => {
            let cell = row.append('td');
            cell.text(value);
        });
    });

});

// Get a reference to the reset button
let resetButton = d3.select('#reset-btn')

// Create a function to reset the table to it's original state 
function resetTable(){
    createTable(tableData);
};

// Assign the resetTable funtion to the resetButton 
resetButton.on("click", resetTable);

// let dateFilter = d3.select("#datetime").property('value');
// let cityFilter = d3.select("#city").property('value');
// let stateFilter = d3.select("#state").property('value');
// let countryFilter = d3.select("#country").property('value');
// let shapeFilter = d3.select("#shape").property('value');
    
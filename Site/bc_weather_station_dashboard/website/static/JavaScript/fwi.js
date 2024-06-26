function updateFWI(value_fwi) {
    // Get the arrow and arrow value elements
    const arrow_fwi = document.getElementById('arrow-fwi');
    const arrowValue_fwi = document.getElementById('arrowValue-fwi');

    if(value_fwi === undefined) {
        arrow_fwi.style.left = 'calc(' + 0 + '% - 14px)';
        arrowValue_fwi.textContent = 'N/A';
        return; // Return early to prevent the rest of the function from running
    }

    value_fwi = Math.round(value_fwi);
    let position_fwi = value_fwi;

    // check if value_FWI is less than 0 and set it to 0
    if(value_fwi < 0) {
        value_fwi = 0;
    }

    // Convert value_fwi to 120 if it is greater than 120 and convert value_fwi to 0 if it is less than 0
    if (position_fwi > 50) {
        position_fwi = 50;
    }
    if (position_fwi < 0) {
        position_fwi = 0;
    }

    // Calculate the top position of the arrow based on the value
    const leftPosition_fwi = 'calc(' + ((position_fwi) * 2) + '% - 14px)'; // Calculate the top position

    // Set the top position of the arrow and display the value
    arrow_fwi.style.left = leftPosition_fwi;
    arrowValue_fwi.textContent = value_fwi;
}

module.exports = { updateFWI };
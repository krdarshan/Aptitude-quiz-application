document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('recruitmentForm');

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const firstPriority = document.getElementById('firstPriority').value;
    const resume = document.getElementById('resume').files[0];

    if (firstPriority === 'web developer') {
      console.log('Saving resume for web developer position');

    
      const jsonData = {
        name: name,
        email: email,
        firstPriority: firstPriority,
        resume: resume.name
      };

    
      downloadJSON(jsonData);
    } else {
      console.log('First priority does not match web developer');
    }

  
    document.getElementById('name').value = '';
    document.getElementById('email').value = '';
    document.getElementById('firstPriority').value = '';
    document.getElementById('resume').value = '';
  });

  // Function to generate JSON and initiate download
  function downloadJSON(data) {
    const jsonDataStr = JSON.stringify(data, null, 2); // Convert data to pretty-printed JSON string
    const blob = new Blob([jsonDataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = 'logic.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }
});

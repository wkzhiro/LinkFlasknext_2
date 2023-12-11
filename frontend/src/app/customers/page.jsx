async function fetchTest(customerId) {
  // const customerId = 'C007';
  const staticData = await fetch(`http://127.0.0.1:5000/customers?customer_id=${customerId}`);
  return staticData.json();
}

export default async function Page() {
  const customerInfo = await fetchTest("C009");
  // return <pre>{JSON.stringify(customerInfo, null, 2)}</pre>
  return (
    <div className="m-4 card bordered bg-blue-100 hover:bg-blue-200 transition-colors duration-200">
      <div className="card-body">
        <h2 className="card-title">{customerInfo[0].customer_name}</h2> 
        <p>Customer ID: {customerInfo[0].customer_id}</p>
        <p>Age: {customerInfo[0].age}</p>
        <p>Gender: {customerInfo[0].gender}</p>
      </div>
    </div>
  )
}
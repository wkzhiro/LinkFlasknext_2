export default async function fetchCustomers() {
    const res = await fetch(process.env.API_ENDPOINT+'/allcustomers', { cache: "no-cache" });
    console.log("API_ENDPOINT",process.env.API_ENDPOINT)
    if (!res.ok) {
      throw new Error('Failed to fetch customers');
    }
    return res.json();
  }
  
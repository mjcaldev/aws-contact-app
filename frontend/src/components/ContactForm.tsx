import { useState } from 'react';
import axios from 'axios';

export default function ContactForm() {
  const [form, setForm] = useState({ name: '', email: '', message: '' });
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus('loading');
    try {
      await axios.post(import.meta.env.VITE_API_URL, form);
      setStatus('success');
      setForm({ name: '', email: '', message: '' });
    } catch {
      setStatus('error');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" onChange={handleChange} value={form.name} required />
      <input name="email" placeholder="Email" onChange={handleChange} value={form.email} required />
      <textarea name="message" placeholder="Message" onChange={handleChange} value={form.message} required />
      <button type="submit">Send</button>
      {status === 'success' && <p className="success">Sent!</p>}
      {status === 'error' && <p className="error">Error sending message.</p>}
    </form>
  );
}
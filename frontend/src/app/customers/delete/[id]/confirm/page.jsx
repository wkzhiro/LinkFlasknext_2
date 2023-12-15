"use client"
import Link from 'next/link';
import { revalidatePath } from 'next/cache';
import { useRouter, useSearchParams } from 'next/navigation';

export default function ConfirmPage(props) {
    const customer_id = useSearchParams().get("customer_id");
    // revalidatePath(`/customers`);
    return (
        <>
            <div className="card bordered bg-white border-blue-200 border-2 max-w-sm m-4">
                <div className="alert alert-success p-4 text-center text-white">
                    {customer_id}を削除しました
                </div>
                <Link href="/customers" className="flex justify-center">
                    <button className="btn btn-outline btn-accent">
                        一覧に戻る
                    </button>
                </Link>
            </div>
        </>
    )
}
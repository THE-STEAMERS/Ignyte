import Link from "next/link";
import { buttonVariants } from "@/components/ui/button";
import Anchor from "@/components/retailer/anchor";

export const NAVLINKS = [
  {
    title: "Dashboard",
    href: "/manufacturer",
  },
  {
    title: "Accounting",
    href: "/manufacturer/accounting",
  },
  {
    title: "StockCount",
    href: "/manufacturer/stockCount",
  },
  {
    title: "Profile",
    href: "/manufacturer/profile",
  },
  {
    title: "Configuration", // New Configuration Route
    href: "/manufacturer/configuration",
  },
];

export function Navbar() {
  return (
    <nav className="w-full border-b h-16 sticky top-0 z-50 bg-gray-900 text-white">
      <div className="sm:container mx-auto w-[95vw] h-full flex items-center justify-between md:gap-2">
        {/* Left Section: Logo and Navigation Menu */}
        <div className="flex items-center gap-8">
          <Logo />
          <NavMenu />
        </div>

        {/* Right Section: Placeholder for future actions (e.g., user profile, notifications) */}
        <div className="flex items-center gap-6">
          {/* Add any right-aligned content here if needed */}
        </div>
      </div>
    </nav>
  );
}

export function Logo() {
  return (
    <Link href="/manufacturer" className="flex items-center gap-2.5">
      <h2 className="text-lg font-bold font-code text-blue-400 hover:text-blue-500 transition-colors">
        Manufacturer
      </h2>
    </Link>
  );
}

export function NavMenu() {
  return (
    <ul className="flex items-center gap-6 text-sm font-medium">
      {NAVLINKS.map((item) => (
        <li key={item.title + item.href}>
          <Anchor
            activeClassName="!text-blue-400 font-semibold"
            absolute
            className="flex items-center gap-1 text-gray-300 hover:text-blue-400 transition-colors"
            href={item.href}
          >
            {item.title}
          </Anchor>
        </li>
      ))}
    </ul>
  );
}